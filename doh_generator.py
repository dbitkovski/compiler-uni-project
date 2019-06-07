from enum import Enum
from models.llvm_scope import Scope_llvm
iter_name = 1
label_name = 1
strings = []
_scopes = []
_cur_scope = None

class Datatype(Enum):
    int = 'i32'
    double = 'double'
    bool = 'i8'
    string = 'i8*'

i_operators = {
    'plus' : 'add',
    'minus' : 'sub',
    'mul' : 'mul',
    'div' : 'sdiv',
    'eq' : 'eq',
    'ne' : 'ne',
    'gt' : 'sgt',
    'ge' : 'sge',
    'lt' : 'slt',
    'le' : 'sle'
}

f_operators = {
    'plus' : 'fadd',
    'munis' : 'fsub',
    'mul' : 'fmul',
    'div' : 'fdiv',
    'eq' : 'oeq',
    'ne' : 'one',
    'gt' : 'ogt',
    'ge' : 'oge',
    'lt' : 'olt',
    'le' : 'ole'
}

# Функция, которая вызывается из main.py
# Возвращает сгенерированный код
def generate_code(ast):
    global _scopes
    global _cur_scope
    _cur_scope = Scope_llvm()
    _scopes.append(_cur_scope)
    commands = create_llvm(ast)
    return commands


# Функция, для прохода по первому уровню дерева
# И всяким доп.штукам, который пока не реализованы
def create_llvm(ast):
    code = ''
    funcs = []
    structure = []
    for node in ast.parts:
        if hasattr(node, 'type'):
            if node.type == 'VARIABLE':
                code = code + decl_var_llvm(node)
            if node.type == 'ASSIGN':
                code = code + assign_llvm(node)
            if node.type == 'FUNCTION':
                funcs.append(decl_func_llvm(node))
            if node.type == 'FUNCTION_CALL':
                var, func_code = llvm_func_call(node)
                code = code + func_code
            if node.type == 'RETURN':
                code = code + llvm_return(node)
            if node.type == 'STRUCTURE':
                structure.append(decl_struct_llvm(node))
            if node.type == 'GOTO':
                code = code + llvm_goto(node)
            if node.type == 'GOTO_MARK':
                code = code + llvm_goto_mark(node)
            if node.type == 'ARRAY':
                code = code + decl_array_llvm(node)
            if node.type == 'IF' or node.type == 'IF_ELSE':
                code += llvm_if(node)
    res = '\n'.join(structure) + '\n'.join(funcs) + '\n'.join(strings) + code
    return res

def llvm_if(node):

    global _cur_scope
    global _scopes
    f = _cur_scope
    _cur_scope = Scope_llvm(f, _cur_scope.variables.copy())
    _scopes.append(_cur_scope)
    #print(10)
    name = get_llvm_var_name()
    code_if = create_llvm(node.parts[1])
    _cur_scope = _cur_scope.scope
    code = f'{name} = icmp eq i32 10, 100 \n'
    try:
        node.parts[2]
    except Exception:
        label_if = get_llvm_label_name()
        label_end = get_llvm_label_name()
        code += f'br i1 {name}, Label {label_if}, Label {label_end} \n' \
                f'{label_if}: \n' \
                f'{code_if}' \
                f'br Label {label_end} \n' \
                f'{label_end}: \n'
    else:
        label_if = get_llvm_label_name()
        label_else = get_llvm_label_name()
        label_end = get_llvm_label_name()
        code_else = create_llvm(node.parts[2])
        _cur_scope = _cur_scope.scope
        code += f'br i1 {name}, Label {label_if}, Label {label_else} \n' \
                f'{label_if}: \n' \
                f'{code_if}' \
                f'br Label {label_else} \n' \
                f'{label_else}: \n' \
                f'{code_else}' \
                f'br Label {label_end} \n' \
                f'{label_end}: \n'
    return code






def decl_struct_llvm(node):

    def get_struct_llvm_params(params):
        return list(map(lambda x: Datatype[x.type].value, params))
    name = get_llvm_var_name()
    global _cur_scope
    llvm_params_list = get_struct_llvm_params(node.parts[1].parts)
    llvm_params_string = ', '.join(llvm_params_list)
    code = f'%{node.parts[0].parts[0]} = type {{ {llvm_params_string} }}'
    _cur_scope.add_variable('struct', name, f'%{name}', llvm_params_list)
    return code

def decl_array_llvm(node):
    name_array = get_llvm_var_name()
    type = Datatype[node.parts[0].parts[0]].value
    size = node.parts[2].parts[0]
    _cur_scope.add_variable(f'{size} x {type}', node.parts[1].parts[0], name_array, {'size': size})
    code = f'{name_array} = alloca [{size} x {type}]\n'
    try:
        node.parts[3]
    except Exception:
        return code
    else:
        elems = list(map(lambda x: x.parts, node.parts[3].parts))
        elems = list(map(lambda x: x[0], elems))
        for i in range(len(elems)):
            name = get_llvm_var_name()
            str = f'{name} = getelementptr inbounds [{size} x {type}], [{size} x {type}]* {name_array}, i8 0, i8 {i} \n' \
                f'store {type} {elems[i]}, {type}* {name} \n'
            code += str
        return code


def decl_func_llvm(node):

    def get_func_llvm_params(params):
        return list(map(lambda x: {'type': Datatype[x.type].value,'name': x.parts[0], 'llvm_name': get_llvm_var_name()}, params))

    def add_params_in_scope(params):
        global _cur_scope
        for p in params:
            _cur_scope.add_variable(p['type'], p['name'], p['llvm_name'])

    global _cur_scope
    global _scopes
    func_type = node.parts[0].parts[0]
    func_name = node.parts[1].parts[0]
    func_params = get_func_llvm_params(node.parts[2].parts)
    llvm_params = []
    for p in func_params:
        llvm_params.append(f'{p["type"]} {p["llvm_name"]}')
    llvm_type = Datatype[func_type].value
    _cur_scope.add_variable(llvm_type, func_name, f'@{func_name}', llvm_params)
    func_title = f'define {llvm_type} @{func_name}({", ".join(llvm_params)}) {{\n'

    f = _cur_scope
    _cur_scope = Scope_llvm(f)
    _scopes.append(_cur_scope)
    add_params_in_scope(func_params)

    func_code = create_llvm(node.parts[3])
    _cur_scope = _cur_scope.scope
    code = func_title + func_code + '}\n'
    return code


def decl_var_llvm(node):
    global _cur_scope
    global strings
    value_type = node.parts[2].type.lower()
    llvm_name, code = llvm_expression(node.parts[0].parts[0], node.parts[2])
    _cur_scope.add_variable(node.parts[0].parts[0], node.parts[1].parts[0], llvm_name)
    if not node.parts[0].parts[0] == 'string':
        return code
    else:
        strings.append(code)
        return ''


def assign_llvm(node):
    global _cur_scope
    var_name = node.parts[0].parts[0]
    var = _cur_scope.get_llvm_var(var_name)
    value = node.parts[1]
    if 'x' in var['type']:
        code = update_array_elem(var, node.parts[1].parts[0], node.parts[2])
    elif 'struct' in var['type']:
        pass
    else:
        llvm_name, code = llvm_expression(var['type'], value)
        _cur_scope.change_llvm_name(var_name, llvm_name)
    return code


def llvm_expression(result_type, expr):
    global _cur_scope
    expr_type = expr.type.lower()
    if expr_type in ['int', 'string', 'double', 'bool']:
        llvm_name, code = decl_const(result_type, expr.parts[0])
    elif expr_type == 'id':
        llvm_name, code = decl_var_id(expr.parts[0])
    elif expr_type == 'function_call':
        llvm_name, code = llvm_func_call(expr)
    elif is_math_oper(expr_type):
        llvm_name, code = math_operations(result_type, expr)
    elif is_logical_oper(expr_type):
        llvm_name, code = logical_operations(expr)
    return (llvm_name, code)


def llvm_func_call(node, res_var=None):
    def get_params_type(func_name):
        global _cur_scope
        res = []
        llvm_var = _cur_scope.get_llvm_var(func_name)
        for par in llvm_var['options']:
            p_type = par.split()[0]
            res.append(p_type)
        return res

    def get_args(args, func_name):
        global _cur_scope
        res = []
        res_code = ''
        params_type = get_params_type(func_name)
        for i in range(len(args)):
            code = ''
            a_type = args[i].type.lower()
            if a_type in ['int', 'string', 'double', 'bool']:
                val = args[i].parts[0]
            elif a_type == 'id':
                llvm_var = _cur_scope.get_llvm_var(args[i].parts[0])
                val = llvm_var['llvm_name']
            else:
                val, code = math_operations(params_type[i], args[i])
            res.append(f'{params_type[i]} {val}')
            if not code == '':
                res_code = res_code + code + '\n'
        return (res, res_code)

    global _cur_scope
    func_name = node.parts[0].parts[0]
    func_type = _cur_scope.get_llvm_var(func_name)['type']
    args, code = get_args(node.parts[1].parts, func_name)
    if res_var is None:
        res_var = get_llvm_var_name()
    ptr = get_llvm_var_name()
    alloca = f'{ptr} = {llvm_alloca(func_type)}\n'
    func_call = f'{res_var} = call {func_type} @{func_name}({", ".join(args)})\n'
    store = f'{llvm_store(func_type, str(res_var), ptr)}\n'
    res = code + alloca + func_call + store
    return (ptr, res)


def llvm_return(node):
    global _cur_scope
    print(node)
    val_type = node.parts[0].type.lower()
    if val_type in ['int', 'double', 'string', 'bool']:
        value = node.parts[0].parts[0]
        return f'ret {Datatype[val_type].value} {value}\n'
    elif val_type == 'id':
        var = node.parts[0].parts[0]
        llvm_var = _cur_scope.get_llvm_var(var)
        return f'ret {llvm_var["type"]} {llvm_var["llvm_name"]}\n'
    else:
        # TODO Написать функцию для получения типа
        llvm_name, code = llvm_expression(node.parts[0])
        

def update_array_elem(array_obj, index, value):
    global _cur_scope
    size = int(array_obj['options']['size'])
    if int(index) >= size:
        raise NameError('Out of range')
    name = array_obj['llvm_name']
    a_type = array_obj['type']
    ptr = get_llvm_var_name()
    el_ptr = f'{ptr} = getelementptr inbounds [{a_type}], [{a_type}]* {name}, i8 0, i8 {index}\n'
    el_type = a_type.split()[2]
    val_ptr, expr_code = llvm_expression(el_type, value)
    el_var = get_llvm_var_name()
    el_val = f'{el_var} = {llvm_load(el_type, val_ptr)}\n'
    store = f'store {el_type} {el_var}, {el_type}* {ptr}\n'
    code = expr_code + el_val + el_ptr + store
    return code

def llvm_goto(node):
    global _cur_scope
    mark_name = node.parts[0].parts[0]
    return f'br label %{mark_name}\n'


def llvm_goto_mark(node):
    global _cur_scope
    mark_name = node.parts[0]
    return f'{mark_name}:\n'



def decl_const(v_type, value):
    '''
    Construct string with variable declaration
    v_type (string) - variable type
    value (string) - variable value
    return - tuple with llvm variable name and code for generating
    '''
    if not v_type == 'string':
        name = get_llvm_var_name()
        if v_type in ['int', 'double', 'bool']:
            llvm_type = Datatype[v_type].value
        else:
            llvm_type = v_type
        alloca = f'{name} = {llvm_alloca(llvm_type)}\n'
        store = f'{llvm_store(llvm_type, str(value), name)}\n'
        code = alloca + store
        return (name, code)
    else:
        name = get_llvm_global_name()
        code = f'{name} = constant [{len(value)+2} x i8] c"{value}\\0A\\00"\n'
        return (name, code)


def decl_var_id(var_name):
    global _cur_scope
    id_llvm_var = _cur_scope.get_llvm_var(var_name, True)
    id_type = id_llvm_var['type']
    id_ptr = id_llvm_var['llvm_name']
    res_ptr = get_llvm_var_name()
    res_val = get_llvm_var_name()
    if not id_type == 'string':
        llvm_type = Datatype[id_type].value
        alloca = f'{res_ptr} = {llvm_alloca(llvm_type)}\n'
        load = f'{res_val} = {llvm_load(llvm_type, id_ptr)}\n'
        store = f'{llvm_store(llvm_type, res_val, res_ptr)}\n'
        code = alloca + load + store
        return (res_ptr, code)
    else:
        return ('', '')


def is_math_oper(operation):
    return operation.lower() in ['plus', 'minus', 'mul', 'div', 'pow', 'int divide', 'modulo']


def is_logical_oper(operation):
    return operation.lower() in ['lor', 'land', 'lt', 'le', 'gt', 'ge', 'eq', 'ne', 'lnot']


def is_bitwise_oper(operation):
    return operation.lower() in ['bor', 'band']


def math_operations(v_type, node):
    l_oper = node.parts[0]
    r_oper = node.parts[1]

    l_ptr, l_code = llvm_expression(v_type, l_oper)
    r_ptr, r_code = llvm_expression(v_type, r_oper)

    if v_type in ['int', 'double', 'string', 'boolean']:
        llvm_type = Datatype[v_type].value
    else:
        llvm_type = v_type
    operation = node.type.lower()

    l_var_name = get_llvm_var_name()
    r_var_name = get_llvm_var_name()
    res_name = get_llvm_var_name()
    l_val = f'{l_var_name} = {llvm_load(llvm_type, l_ptr)}\n'
    r_val = f'{r_var_name} = {llvm_load(llvm_type, r_ptr)}\n'
    res_ptr = f'{res_name} = {llvm_alloca(llvm_type)}\n'
    res_name_2 = get_llvm_var_name()
    res = f'{res_name_2} = {llvm_math_action(operation, llvm_type, l_var_name, r_var_name)}\n'
    res_store = f'{llvm_store(llvm_type, res_name_2, res_name)}\n'
    code = l_code + r_code + l_val + r_val + res_ptr + res + res_store
    return (res_name, code) 


def logical_operations(node):
    global _cur_scope
    l_oper = node.parts[0]
    r_oper = node.parts[1]

    l_oper_type = l_oper.type.lower()
    r_oper_type = l_oper.type.lower()

    if is_atom(l_oper.type.lower()):
        l_ptr, l_code = decl_const(l_oper_type, l_oper.parts[0])
    elif l_oper.type.lower() == 'id':
        l_ptr, l_code = decl_var_id(l_oper_type, l_oper.parts[0])
    else:
        l_ptr, l_code = logical_operations(l_oper)

    if is_atom(r_oper.type.lower()):
        r_ptr, r_code = decl_const(r_oper_type, r_oper.parts[0])
    elif r_oper.type.lower() == 'id':
        r_ptr, r_code = decl_var_id(r_oper_type, r_oper.parts[0])
    else:
        r_ptr, r_code = logical_operations(r_oper)

    if l_oper_type in ['int', 'double', 'boolean']:
        llvm_type = Datatype[l_oper_type].value
    else:
        llvm_type = l_oper_type

    operation = node.type.lower()
    
    l_var_name = get_llvm_var_name()
    r_var_name = get_llvm_var_name()
    res_name = get_llvm_var_name()
    l_val = f'{l_var_name} = {llvm_load(llvm_type, l_ptr)}\n'
    r_val = f'{r_var_name} = {llvm_load(llvm_type, r_ptr)}\n'
    res_ptr = f'{res_name} = {llvm_alloca("i1")}\n'
    res_name_2 = get_llvm_var_name()
    res = f'{res_name_2} = {llvm_logic_action(operation, llvm_type, l_var_name, r_var_name)}\n'
    res_store = f'{llvm_store("i1", res_name_2, res_name)}\n'
    code = l_code + r_code + l_val + r_val + res_ptr + res + res_store
    return (res_name, code) 


def is_atom(type):
    return type in ['int', 'double', 'string', 'bool']


def llvm_math_action(op, llvm_type, a, b):
    if not op == 'pow':
        llvm_oper = i_operators[op] if llvm_type == 'i32' else f_operators[op]
        return f'{llvm_oper} {llvm_type} {a}, {b}'
    else:
        return f'call double @llvm.powi.f64(double {a}, i32 {b})'


def llvm_logic_action(op, llvm_type, a, b):
    llvm_oper = f'icmp {i_operators[op]}' if llvm_type in ['i1', 'i32'] else f'fcmp {f_operators[op]}'
    return f'{llvm_oper} {llvm_type} {a}, {b}'


# Some helpful functions to do basic llvm operations
def llvm_load(v_type, ptr):
    return f'load {v_type}, {v_type}* {ptr}'

def llvm_store(v_type, value, ptr):
    return f'store {v_type} {value}, {v_type}* {ptr}'

def llvm_alloca(v_type):
    return f'alloca {v_type}'


# Create variable name for llvm code using global variable 'iter_name'
# return {string} - '%.number'
def get_llvm_var_name():
    global iter_name
    name = f'%.{iter_name}'
    iter_name += 1
    return name

def get_llvm_global_name():
    global iter_name
    name = f'@.{iter_name}'
    iter_name += 1
    return name

def get_llvm_label_name():
    global label_name
    name = f'label{label_name}'
    label_name += 1
    return name
import ply.yacc as yacc
from errors import error
from models.node import Node
from doh_lexer import tokens

# All operations(math or logical) with numbers are defined at the 'expr' rule
# All conditionals are defined at the 'expr' rule too
# The 'stmt' rule is needed for storing statements like some expression or assignment.
# It's expanding
# The 'stmtList' rule is needed for storing expressions that were defined as 'stmt'. It's the main rule at the
# parser for now.

# Precedence is tuple to keep precedence level and associativity of tokens.
# Values are in ascending precedent level. Comma has lower priority, lbrace, rbrace ... have higher priority.

precedence = (
    ('left', 'COMMA'),
    ('right', 'EQUALS'),
    ('nonassoc', 'LOR'),
    ('nonassoc', 'LAND'),
    ('nonassoc', 'BOR'),
    ('nonassoc', 'BAND'),
    ('nonassoc', 'EQ', 'NE'),
    ('nonassoc', 'LE', 'GE', 'LT', 'GT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MUL', 'DIVIDE', 'INTDIVIDE', 'MODULO'),
    ('right', 'POW'),
    ('right', 'UMINUS', 'LNOT'),
    ('left', 'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'DOT')
)


def p_program(p):
    '''
    program :
            | scope
    '''
    if len(p) == 1:
        p[0] = ''
    elif len(p) == 2:
        p[0] = p[1]


def p_body_block(p):
    'basic_block : LBRACE scope RBRACE'
    p[0] = p[2]


def p_body_block_error(p):
    '''
    basic_block : error scope RBRACE
                | LBRACE error RBRACE
                | LBRACE scope error
    '''
    if str(p.slice[1]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is "{"' % p.slice[1].value.value)
    elif str(p.slice[2]) == 'error':
        print('Unexpected symbol "%s". Expected statement' % p.slice[2].value.value)
    elif str(p.slice[3]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is "}"' % p.slice[3].value.value)


def p_func_declaration(p):
    'func_declaration : FUNCTION datatype id LPAREN params RPAREN basic_block'
    p[0] = Node('FUNCTION', [p[2], p[3], p[5], p[7]], p.lineno(1))


def p_func_declaration_error(p):
    '''
    func_declaration : error datatype id LPAREN params RPAREN basic_block
                     | FUNCTION error id LPAREN params RPAREN basic_block
                     | FUNCTION datatype error LPAREN params RPAREN basic_block
                     | FUNCTION datatype id error params RPAREN basic_block
                     | FUNCTION datatype id LPAREN params error basic_block
    '''
    if str(p.slice[1]) == 'error':
        print('Unexpected symbol "%s". Expected token is "function"' % p.slice[1].value.value)
    elif str(p.slice[2]) == 'error':
        print('Unexpected symbol "%s". Expected "datatype" of function' % p.slice[2].value.value)
    elif str(p.slice[3]) == 'error':
        print('Unexpected symbol "%s". Expected token is "ID"' % p.slice[3].value.value)
    elif str(p.slice[4]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is "("' % p.slice[4].value.value)
    elif str(p.slice[6]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is ")"' % p.slice[6].value.value)


def p_scope(p):
    '''
    scope : scope statement
          | statement
    '''
    if len(p) == 3:
        p[0] = p[1].add_parts([p[2]])
    else:
        p[0] = Node('SCOPE', [p[1]], 0)


def p_stmt(p):
    '''
    statement : expr SEMI
              | var_declaration
              | return
              | assign
              | func_declaration
              | struct_declaration
              | while
              | BREAK SEMI
              | CONTINUE SEMI
              | GOTO ID SEMI
              | goto_mark
              | if-else
    '''
    if p[1] == 'break':
        p[0] = Node('BREAK', [], p.lineno(1))
    elif p[1] == 'continue':
        p[0] = Node('CONTINUE', [], p.lineno(1))
    elif p[1] == 'goto':
        p[0] = Node('GOTO', [p[2]], p.lineno(1))
    else:
        p[0] = p[1]


def p_loops(p):
    '''
    while : WHILE conditional basic_block
          | DO basic_block WHILE conditional SEMI
    '''
    if len(p) == 4:
        p[0] = Node('WHILE', [p[2], p[3]], p.lineno(1))
    else:
        p[0] = Node('DO_WHILE', [p[2], p[4]], p.lineno(5))


def p_loop_dowhile_error(p):
    '''
    while : error basic_block WHILE conditional SEMI
          | DO basic_block error conditional SEMI
          | DO basic_block WHILE conditional error
    '''
    if str(p.slice[1]) == 'error':
        print('Unexpected token "%s". Expected token is "DO"' % p.slice[1].value.value)
    elif str(p.slice[3]) == 'error':
        print('Unexpected token "%s". Expected token is "WHILE"' % p.slice[3].value.value)
    elif str(p.slice[5]) == 'error':
        print('Unexpected token "%s". Expected token is ";"' % p.slice[5].value.value)

def p_if_else(p):
    '''
    if-else : IF conditional basic_block
            | IF conditional basic_block ELSE basic_block
    '''
    if len(p) == 4:
        p[0] = Node('IF', [p[2], p[3]], p.lineno(1))
    else:
        p[0] = Node('IF_ELSE', [p[2], p[3], p[5]], p.lineno(1))


def p_conditional(p):
    'conditional : LPAREN expr RPAREN'
    p[0] = p[2]


def p_conditional_errors(p):
    '''
    conditional : error expr RPAREN
                | LPAREN error RPAREN
                | LPAREN expr error
    '''
    if str(p.slice[1]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is "("' % p.slice[1].value.value)
    elif str(p.slice[2]) == 'error':
        print('Unexpected symbol "%s". Expected expression' % p.slice[2].value.value)
    elif str(p.slice[3]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is ")"' % p.slice[3].value.value)


def p_struct_declaration(p):
    'struct_declaration : STRUCTURE id LBRACE struct_params RBRACE'
    p[0] = Node('STRUCTURE', [p[2], p[4]], p.lineno(1))


def p_struct_declaration_error(p):
    '''
    struct_declaration : STRUCTURE error LBRACE struct_params RBRACE
                       |  STRUCTURE id error struct_params RBRACE
                       |  STRUCTURE id LBRACE struct_params error
    '''
    if str(p.slice[2]) == 'error':
        print('Unexpected symbol "%s". Expected token is "ID"' % p.slice[2].value.value)
    elif str(p.slice[3]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is "{"' % p.slice[3].value.value)
    elif str(p.slice[5]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is "}"' % p.slice[5].value.value)


def p_struct_params(p):
    '''
    struct_params : struct_param
                  | struct_params COMMA struct_param
    '''
    if len(p) == 2:
        p[0] = Node('PARAMS', [p[1]], p.lineno(1))
    else:
        p[0] = p[1].add_parts([p[3]])


def p_struct_params_error(p):
    'struct_params : struct_params error struct_param'
    print('Unexpected symbol "%s". Expected symbol is ","' % p.slice[2].value.value)


def p_struct_param(p):
    'struct_param : DATATYPE ID'
    p[0] = Node(p[1], [p[2]], p.lineno(1))


def p_struct_param_error(p):
    '''
    struct_param : error ID
                 | DATATYPE error
    '''
    if str(p.slice[1]) == 'error':
        print('Unexpected symbol "%s". Expected "DATATYPE" of parameter ' % p.slice[1].value.value)
    elif str(p.slice[2]) == 'error':
        print('Unexpected symbol "%s". Expected token is "ID"' % p.slice[2].value.value)


def p_params(p):
    '''
    params :
           | param
           | params COMMA param
    '''
    if len(p) == 1:
        p[0] = Node('PARAMS', [])
    elif len(p) == 2:
        p[0] = Node('PARAMS', [p[1]], p.lineno(1))
    else:
        p[0] = p[1].add_parts([p[3]])


def p_params_error(p):
    'params : params error param'
    print('Unexpected symbol "%s". Expected symbol is ","' % p.slice[1].value.value)


def p_param_declaration(p):
    'param : DATATYPE ID'
    p[0] = Node(p[1], [p[2]], p.lineno(1))


def p_param_declaration_error(p):
    '''
    param : error ID
          | DATATYPE error
    '''
    if str(p.slice[1]) == 'error':
        print('Unexpected symbol "%s". Expected "DATATYPE" of parameter' % p.slice[1].value.value)
    elif str(p.slice[2]) == 'error':
        print('Unexpected symbol "%s". Expected token is "ID"' % p.slice[2].value.value)


def p_func_call(p):
    'expr : id LPAREN args RPAREN'
    p[0] = Node('FUNCTION_CALL', [p[1], p[3]], p.lineno(1))


def p_func_call_error(p):
    '''
    expr : id error args RPAREN
         | id LPAREN args error
    '''
    if str(p.slice[2]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is "("' % p.slice[2].value.value)
    elif str(p.slice[4]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is ")"' % p.slice[4].value.value)


def p_arguments(p):
    '''
    args :
         | expr
         | args COMMA expr
    '''
    if len(p) == 1:
        p[0] = Node('ARGUMENTS', [])
    elif len(p) == 2:
        p[0] = Node('ARGUMENTS', [p[1]], p.lineno(1))
    elif len(p) == 4:
        p[0] = p[1].add_parts([p[3]])


def p_arguments_error(p):
    'args : args error expr'
    print('Unexpected symbol "%s". Expected symbol is ","' % p.slice[2].value.value)


def p_var_declaration(p):
    '''
    var_declaration : datatype id EQUALS expr SEMI
                    | datatype id SEMI
    '''
    if len(p) == 6:
        p[0] = Node('VARIABLE', [p[1], p[2], p[4]], p.lineno(3))
    else:
        p[0] = Node('VARIABLE', [p[1], p[2]], p.lineno(3))


def p_struct_var_declaration(p):
    '''
    var_declaration : ID id SEMI
                    | ID id EQUALS LBRACE args RBRACE SEMI
                    | ID id EQUALS expr SEMI
    '''
    if len(p) == 4:
        p[0] = Node('STRUCT_VAR', [Node('TYPE', [p[1]]), p[2]], p.lineno(1))
    elif len(p) == 8:
        p[0] = Node('STRUCT_VAR', [Node('TYPE', [p[1]]), p[2], p[5]], p.lineno(1))
    else:
        p[0] = Node('STRUCT_VAR', [Node('TYPE', [p[1]]), p[2], p[4]], p.lineno(1))


def p_var_declaration_error_1(p):
    '''
    var_declaration : datatype error EQUALS expr SEMI
                    | datatype id error expr SEMI
                    | datatype id EQUALS expr error
                    | datatype id EQUALS error SEMI
    '''
    if str(p.slice[2]) == 'error':
        print('Unexpected symbol "%s". Expected token is "ID"' % p.slice[2].value.value)
    elif str(p.slice[3]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is "="' % p.slice[3].value.value)
    elif str(p.slice[5]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is ";"' % p.slice[5].value.value)
    elif str(p.slice[4]) == 'error':
        print('Unexpected symbol "%s". Expected expression for variable' % p.slice[4].value.value)


def p_var_declaration_error_2(p):
    '''
    var_declaration : datatype error SEMI
                    | datatype id error
    '''
    if str(p.slice[2]) == 'error':
        print('Unexpected symbol "%s". Expected token is "ID"' % p.slice[2].value.value)
    elif str(p.slice[3]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is ";"' % p.slice[3].value.value)


def p_var_declaration_error_3(p):
    '''
    var_declaration : ID error EQUALS LBRACE args RBRACE SEMI
                    | ID id error LBRACE args RBRACE SEMI
                    | ID id EQUALS error args RBRACE SEMI
                    | ID id EQUALS LBRACE error RBRACE SEMI
                    | ID id EQUALS LBRACE args error SEMI
                    | ID id EQUALS LBRACE args RBRACE error
    '''
    if str(p.slice[2]) == 'error':
        print('Unexpected symbol "%s". Expected token is "ID"' % p.slice[2].value.value)
    elif str(p.slice[3]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is "="' % p.slice[3].value.value)
    elif str(p.slice[4]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is "{"' % p.slice[4].value.value)
    elif str(p.slice[5]) == 'error':
        print('Unexpected symbol "%s". Expected arguments for structure"' % p.slice[5].value.value)
    elif str(p.slice[6]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is "}"' % p.slice[6].value.value)
    elif str(p.slice[7]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is ";"' % p.slice[7].value.value)


def p_var_assign(p):
    'assign : id EQUALS expr SEMI'
    if len(p) == 5:
        p[0] = Node('ASSIGN', [p[1], p[3]], p.lineno(1))


def p_struct_assign(p):
    '''
    assign : id EQUALS LBRACE args RBRACE SEMI
           | id DOT ID EQUALS expr SEMI
    '''
    if not p[2] == '.':
        p[0] = Node('ASSIGN', [p[1], p[4]])
    else:
        p[0] = Node('ASSIGN', [p[1], p[3], p[5]])


def p_array_assign(p):
    'assign : id LBRACKET expr RBRACKET EQUALS expr SEMI'
    p[0] = Node('ASSIGN', [p[1], p[3], p[6]])


def p_array_assign_error(p):
    '''
    assign : error LBRACKET expr RBRACKET EQUALS expr SEMI
           | id error expr RBRACKET EQUALS expr SEMI
           | id LBRACKET error RBRACKET EQUALS expr SEMI
           | id LBRACKET expr error EQUALS expr SEMI
           | id LBRACKET expr RBRACKET error expr SEMI
           | id LBRACKET expr RBRACKET EQUALS error SEMI
           | id LBRACKET expr RBRACKET EQUALS expr error
    '''
    if str(p.slice[1]) == 'error':
        print('Unexpected symbol "%s". Expected token is "ID"' % p.slice[1].value.value)
    elif str(p.slice[2]) == 'error':
        print('Unexpected symbol "%s". Expected token is "["' % p.slice[2].value.value)
    elif str(p.slice[3]) == 'error':
        print('Unexpected symbol "%s". Expected expression' % p.slice[3].value.value)
    elif str(p.slice[4]) == 'error':
        print('Unexpected symbol "%s". Expected token is "]"' % p.slice[4].value.value)
    elif str(p.slice[5]) == 'error':
        print('Unexpected symbol "%s". Expected token is "="' % p.slice[5].value.value)
    elif str(p.slice[6]) == 'error':
        print('Unexpected symbol "%s". Expected expression for assign' % p.slice[6].value.value)
    elif str(p.slice[7]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is ";"' % p.slice[7].value.value)


def p_assign_error_1(p):
    '''
    assign : ID error expr SEMI
           | ID EQUALS error SEMI
           | ID EQUALS expr error
    '''
    if str(p.slice[2]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is "="' % p.slice[2].value.value)
    elif str(p.slice[3]) == 'error':
        print('Unexpected symbol "%s". Expected expression' % p.slice[3].value.value)
    elif str(p.slice[4]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is ";"' % p.slice[4].value.value)


def p_assign_error_2(p):
    '''
    assign : ID error LBRACE args RBRACE SEMI
           | ID EQUALS error args RBRACE SEMI
           | ID EQUALS LBRACE error RBRACE SEMI
           | ID EQUALS LBRACE args error SEMI
           | ID EQUALS LBRACE args RBRACE error
    '''
    if str(p.slice[2]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is "="' % p.slice[2].value.value)
    elif str(p.slice[3]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is "{"' % p.slice[3].value.value)
    elif str(p.slice[4]) == 'error':
        print('Unexpected symbol "%s". Expected arguments for structure' % p.slice[4].value.value)
    elif str(p.slice[5]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is "}"' % p.slice[5].value.value)
    elif str(p.slice[6]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is ";"' % p.slice[6].value.value)


def p_assign_error_3(p):
    '''
    assign : ID DOT ID error expr SEMI
           | ID DOT ID EQUALS error SEMI
           | ID DOT ID EQUALS expr error
    '''
    if str(p.slice[4]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is "="' % p.slice[4].value.value)
    elif str(p.slice[5]) == 'error':
        print('Unexpected symbol "%s". Expected expression for assign' % p.slice[5].value.value)
    elif str(p.slice[6]) == 'error':
        print('Unexpected symbol "%s". Expected symbol is ";"' % p.slice[6].value.value)


def p_return(p):
    '''
    return : RETURN expr SEMI
           | RETURN SEMI
    '''
    if len(p) == 4:
        p[0] = Node('RETURN', [p[2]], p.lineno(1))
    else:
        p[0] = Node('RETURN', [], p.lineno(1))


def p_return_error(p):
    'return : RETURN error'
    print('Unexpected symbol "%s". Expected symbol is ";"' % p.slice[2].value.value)


def p_math_expressions(p):
    '''
    expr : expr PLUS expr
         | expr MINUS expr
         | expr MUL expr
         | expr DIVIDE expr
         | expr INTDIVIDE expr
         | expr MODULO expr
         | expr POW expr
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if p[2] == '+':
            p[0] = Node('PLUS', [p[1], p[3]], p.lineno(2))
        elif p[2] == '-':
            p[0] = Node('MINUS', [p[1], p[3]], p.lineno(2))
        elif p[2] == '*':
            p[0] = Node('MUL', [p[1], p[3]], p.lineno(2))
        elif p[2] == '/':
            p[0] = Node('DIV', [p[1], p[3]], p.lineno(2))
        elif p[2] == '%':
            p[0] = Node('INT DIVIDE', [p[1], p[3]], p.lineno(2))
        elif p[2] == '%%':
            p[0] = Node('MODULO', [p[1], p[3]], p.lineno(2))
        elif p[2] == '**':
            p[0] = Node('POW', [p[1], p[3]], p.lineno(2))


def p_conditionals(p):
    '''
    expr : expr LE expr
         | expr GE expr
         | expr LT expr
         | expr GT expr
         | expr EQ expr
         | expr NE expr
    '''
    if p[2] == '<=':
        p[0] = Node('LESS OR EQ', [p[1], p[3]], p.lineno(2))
    elif p[2] == '>=':
        p[0] = Node('GREATER OR EQ', [p[1], p[3]], p.lineno(2))
    elif p[2] == '<':
        p[0] = Node('LESS', [p[1], p[3]], p.lineno(2))
    elif p[2] == '>':
        p[0] = Node('GREATER', [p[1], p[3]], p.lineno(2))
    elif p[2] == '==':
        p[0] = Node('EQUALS', [p[1], p[3]], p.lineno(2))
    elif p[2] == '!=':
        p[0] = Node('NOT EQUALS', [p[1], p[3]], p.lineno(2))


def p_expr_error(p):
    'expr : expr error expr'
    print('Unexpected symbol "%s". Expected arithmetic or logical operator' % p.slice[2].value.value)


def p_logical_operation(p):
    '''
    expr : MINUS expr %prec UMINUS
         | expr LAND expr
         | expr LOR expr
         | LNOT expr
    '''
    if p[1] == '-':
        p[0] = Node('UMINUS', [p[2]], p.lineno(1))
    elif p[2] == '&&':
        p[0] = Node('LAND', [p[1], p[3]], p.lineno(1))
    elif p[2] == '||':
        p[0] = Node('LOR', [p[1], p[3]], p.lineno(1))
    elif p[1] == '!':
        p[0] = Node('LNOT', [p[2]], p.lineno(1))


def p_bitwise_operation(p):
    '''
    expr : expr BAND expr
         | expr BOR expr
    '''
    if p[2] == '&':
        p[0] = Node('BAND', [p[1], p[3]], p.lineno(1))
    elif p[2] == '|':
        p[0] = Node('BOR', [p[1], p[3]], p.lineno(1))


def p_literals(p):
    '''
    expr : id
         | int
         | double
         | bool
         | str
         | void
         | NULL
         | LPAREN expr RPAREN
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_const_int(p):
    'int : INTEGER'
    p[0] = Node('INT', [p[1]], p.lineno(1))


def p_const_double(p):
    'double : DOUBLE'
    p[0] = Node('DOUBLE', [p[1]], p.lineno(1))


def p_const_bool(p):
    'bool : BOOL'
    p[0] = Node('BOOL', [p[1]], p.lineno(1))


def p_const_string(p):
    'str : STRING'
    p[0] = Node('STRING', [p[1]], p.lineno(1))


def p_void(p):
    'void : VOID'
    p[0] = Node('VOID', [p[1]], p.lineno(1))


def p_array_init(p):
    '''
    expr : datatype id LBRACKET INTEGER RBRACKET SEMI
         | ID id LBRACKET INTEGER RBRACKET SEMI
         | datatype id LBRACKET INTEGER RBRACKET EQUALS LBRACE args RBRACE SEMI
         | ID id LBRACKET INTEGER RBRACKET EQUALS LBRACE args RBRACE SEMI
    '''
    if len(p) == 6:
        if hasattr(p[1], 'type'):
            p[0] = Node('ARRAY', [p[1], p[2], Node('SIZE', [p[4]])], p.lineno(1))
        else:
            p[0] = Node('ARRAY', [Node('TYPE', [p[1]]), p[2], Node('SIZE', [p[4]])], p.lineno(1))
    else:
        if hasattr(p[1], 'type'):
            p[0] = Node('ARRAY', [p[1], p[2], Node('SIZE', [p[4]]), p[8]], p.lineno(1))
        else:
            p[0] = Node('ARRAY', [Node('TYPE',[p[1]]), p[2], Node('SIZE', [p[4]]), p[8]], p.lineno(1))


def p_array_init_error_1(p):
    '''
    expr : error id LBRACKET INTEGER RBRACKET SEMI
         | datatype error LBRACKET INTEGER RBRACKET SEMI
         | datatype id error INTEGER RBRACKET SEMI
         | datatype id LBRACKET error RBRACKET SEMI
         | datatype id LBRACKET INTEGER error SEMI
         | datatype id LBRACKET INTEGER RBRACKET error
    '''
    if str(p.slice[1]) == 'error':
        print('Unexpected symbol "%s". Expected datatype of array' % p.slice[1].value.value)
    elif str(p.slice[2]) == 'error':
        print('Unexpected symbol "%s". Expected token is "ID"' % p.slice[2].value.value)
    elif str(p.slice[3]) == 'error':
        print('Unexpected symbol "%s". Expected token is "["' % p.slice[3].value.value)
    elif str(p.slice[4]) == 'error':
        print('Unexpected symbol "%s". Expected size of array' % p.slice[4].value.value)
    elif str(p.slice[5]) == 'error':
        print('Unexpected symbol "%s". Expected token is "]"' % p.slice[5].value.value)
    elif str(p.slice[6]) == 'error':
        print('Unexpected symbol "%s". Expected token is ";"' % p.slice[6].value.value)


def p_array_init_error_2(p):
    '''
    expr : ID id error INTEGER RBRACKET SEMI
         | ID id LBRACKET error RBRACKET SEMI
         | ID id LBRACKET INTEGER error SEMI
         | ID id LBRACKET INTEGER RBRACKET error
    '''
    if str(p.slice[3]) == 'error':
        print('Unexpected symbol "%s". Expected token is "["' % p.slice[3].value.value)
    elif str(p.slice[4]) == 'error':
        print('Unexpected symbol "%s". Expected size of array' % p.slice[4].value.value)
    elif str(p.slice[5]) == 'error':
        print('Unexpected symbol "%s". Expected token is "]"' % p.slice[5].value.value)
    elif str(p.slice[6]) == 'error':
        print('Unexpected symbol "%s". Expected token is ";"' % p.slice[6].value.value)


def p_array_init_error_3(p):
    '''
    expr : datatype id error INTEGER RBRACKET EQUALS LBRACE args RBRACE SEMI
         | datatype id LBRACKET error RBRACKET EQUALS LBRACE args RBRACE SEMI
         | datatype id LBRACKET INTEGER error EQUALS LBRACE args RBRACE SEMI
         | datatype id LBRACKET INTEGER RBRACKET error LBRACE args RBRACE SEMI
         | datatype id LBRACKET INTEGER RBRACKET EQUALS error args RBRACE SEMI
         | datatype id LBRACKET INTEGER RBRACKET EQUALS LBRACE error RBRACE SEMI
         | datatype id LBRACKET INTEGER RBRACKET EQUALS LBRACE args error SEMI
         | datatype id LBRACKET INTEGER RBRACKET EQUALS LBRACE args RBRACE error
    '''
    if str(p.slice[3]) == 'error':
        print('Unexpected symbol "%s". Expected token is "["' % p.slice[3].value.value)
    elif str(p.slice[4]) == 'error':
        print('Unexpected symbol "%s". Expected size of array' % p.slice[4].value.value)
    elif str(p.slice[5]) == 'error':
        print('Unexpected symbol "%s". Expected token is "]"' % p.slice[5].value.value)
    elif str(p.slice[6]) == 'error':
        print('Unexpected symbol "%s". Expected token is "="' % p.slice[6].value.value)
    elif str(p.slice[7]) == 'error':
        print('Unexpected symbol "%s". Expected token is "{"' % p.slice[7].value.value)
    elif str(p.slice[8]) == 'error':
        print('Unexpected symbol "%s". Expected arguments' % p.slice[8].value.value)
    elif str(p.slice[9]) == 'error':
        print('Unexpected symbol "%s". Expected token is "}"' % p.slice[9].value.value)
    elif str(p.slice[10]) == 'error':
        print('Unexpected symbol "%s". Expected token is ";"' % p.slice[10].value.value)


def p_array_init_error_4(p):
    '''
    expr : ID id error INTEGER RBRACKET EQUALS LBRACE args RBRACE SEMI
         | ID id LBRACKET error RBRACKET EQUALS LBRACE args RBRACE SEMI
         | ID id LBRACKET INTEGER error EQUALS LBRACE args RBRACE SEMI
         | ID id LBRACKET INTEGER RBRACKET error LBRACE args RBRACE SEMI
         | ID id LBRACKET INTEGER RBRACKET EQUALS error args RBRACE SEMI
         | ID id LBRACKET INTEGER RBRACKET EQUALS LBRACE error RBRACE SEMI
         | ID id LBRACKET INTEGER RBRACKET EQUALS LBRACE args error SEMI
         | ID id LBRACKET INTEGER RBRACKET EQUALS LBRACE args RBRACE error
    '''
    if str(p.slice[3]) == 'error':
        print('Unexpected symbol "%s". Expected token is "["' % p.slice[3].value.value)
    elif str(p.slice[4]) == 'error':
        print('Unexpected symbol "%s". Expected size of array' % p.slice[4].value.value)
    elif str(p.slice[5]) == 'error':
        print('Unexpected symbol "%s". Expected token is "]"' % p.slice[5].value.value)
    elif str(p.slice[6]) == 'error':
        print('Unexpected symbol "%s". Expected token is "="' % p.slice[6].value.value)
    elif str(p.slice[7]) == 'error':
        print('Unexpected symbol "%s". Expected token is "{"' % p.slice[7].value.value)
    elif str(p.slice[8]) == 'error':
        print('Unexpected symbol "%s". Expected arguments' % p.slice[8].value.value)
    elif str(p.slice[9]) == 'error':
        print('Unexpected symbol "%s". Expected token is "}"' % p.slice[9].value.value)
    elif str(p.slice[10]) == 'error':
        print('Unexpected symbol "%s". Expected token is ";"' % p.slice[10].value.value)


def p_index(p):
    'expr : id LBRACKET expr RBRACKET'
    p[0] = Node('ARRAY_ELEMENT', [p[1], p[3]], p.lineno(1))


def p_struct_field(p):
    'expr : id DOT ID'
    p[0] = Node('STRUCT_FIELD', [p[1], p[3]])


def p_goto_mark(p):
    'goto_mark : ID COLON'
    p[0] = Node('GOTO_MARK', [p[1]], p.lineno(1))


def p_datatype(p):
    'datatype : DATATYPE'
    p[0] = Node('TYPE', [p[1]], p.lineno(1))


def p_id(p):
    'id : ID'
    p[0] = Node('ID', [p[1]], p.lineno(1))


def p_error(p):
    if p:
        #error(p.lineno, "Unexpected symbol '%s'" % p.value)
        pass
    else:
        error("End of file", "Syntax error. No more input.")


# Create parser object
def create_doh_parser():
    return yacc.yacc(debug=1)

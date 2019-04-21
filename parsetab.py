
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCOMMArightEQUALSnonassocLORnonassocLANDnonassocBORnonassocBANDnonassocEQNEnonassocLEGELTGTleftPLUSMINUSleftMULDIVIDEINTDIVIDEMODULOrightPOWrightUMINUSLNOTleftLBRACERBRACELPARENRPARENLBRACKETRBRACKETBAND BOOL BOR BREAK COLON COMMA COMMENT CONTINUE DATATYPE DIVIDE DO DOT DOUBLE ELSE EQ EQUALS ERROR FUNCTION GE GOTO GT ID IF INTDIVIDE INTEGER LAND LBRACE LBRACKET LE LNOT LOR LPAREN LT MINUS MODULO MUL NE NEWLINE NULL PLUS POW RBRACE RBRACKET RETURN RPAREN SEMI STRING STRUCTURE VOID WHILEprogram :\n               | basic_blockbasic_block : stmt_listfunc_declaration : FUNCTION datatype id LPAREN params RPAREN LBRACE basic_block RBRACEstmt_list : stmt_list statement\n                 | statement\n    statement : expr SEMI\n              | var_declaration\n              | return\n              | assign\n              | func_declaration\n              | struct_declaration\n              | while\n              | BREAK SEMI\n              | CONTINUE SEMI\n              | GOTO ID SEMI\n              | goto_mark\n              | if-else\n    \n    while : WHILE LPAREN expr RPAREN LBRACE stmt_list RBRACE\n          | DO LBRACE stmt_list RBRACE WHILE LPAREN expr RPAREN SEMI\n    \n    if-else : IF LPAREN expr RPAREN LBRACE stmt_list RBRACE\n            | IF LPAREN expr RPAREN LBRACE stmt_list RBRACE ELSE LBRACE stmt_list RBRACE\n    \n    struct_declaration : STRUCTURE id LBRACE struct_params RBRACE\n    \n    struct_params : struct_param\n                  | struct_params COMMA struct_param\n    \n    struct_param : DATATYPE ID\n                 | func_declaration\n    params :\n              | param\n              | params COMMA paramparam : DATATYPE IDexpr : ID LPAREN args RPARENargs :\n            | expr\n            | args COMMA expr\n    var_declaration : datatype id EQUALS expr SEMI\n                    | datatype id SEMI\n                    | ID id EQUALS LBRACE args RBRACE SEMI\n    assign : ID EQUALS expr SEMI\n              | ID EQUALS LBRACE args RBRACE SEMI\n              | ID DOT ID EQUALS expr SEMI\n    return : RETURN expr SEMI\n           | RETURN SEMI\n    expr : expr PLUS expr\n            | expr MINUS expr\n            | expr MUL expr\n            | expr DIVIDE expr\n            | expr INTDIVIDE expr\n            | expr MODULO expr\n            | expr POW exprexpr : expr LE expr\n            | expr GE expr\n            | expr LT expr\n            | expr GT expr\n            | expr EQ expr\n            | expr NE exprexpr : MINUS expr %prec UMINUS\n            | expr LAND expr\n            | expr LOR expr\n            | LNOT expr\n    expr : expr BAND expr\n         | expr BOR expr\n    expr : id\n            | int\n            | double\n            | bool\n            | str\n            | void\n            | NULL\n            | LPAREN expr RPARENint : INTEGERdouble : DOUBLEbool : BOOLstr : STRINGvoid : VOID\n    expr : datatype LBRACKET RBRACKET id\n         | datatype LBRACKET RBRACKET id EQUALS datatype LBRACKET INTEGER RBRACKET\n    expr : ID LBRACKET expr RBRACKETgoto_mark : ID COLONdatatype : DATATYPEid : ID'
    
_lr_action_items = {'$end':([0,1,2,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,101,112,113,123,141,145,152,153,162,166,168,174,175,178,],[-1,0,-2,-3,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-79,-43,-16,-37,-42,-39,-36,-23,-40,-41,-38,-19,-21,-4,-20,-22,]),'BREAK':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,82,101,112,113,117,123,141,145,148,150,152,153,159,161,162,164,166,168,174,175,176,177,178,],[12,12,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-79,-43,12,-16,-37,-42,12,-39,-36,-23,12,12,-40,-41,12,12,-38,12,-19,-21,-4,-20,12,12,-22,]),'CONTINUE':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,82,101,112,113,117,123,141,145,148,150,152,153,159,161,162,164,166,168,174,175,176,177,178,],[13,13,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-79,-43,13,-16,-37,-42,13,-39,-36,-23,13,13,-40,-41,13,13,-38,13,-19,-21,-4,-20,13,13,-22,]),'GOTO':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,82,101,112,113,117,123,141,145,148,150,152,153,159,161,162,164,166,168,174,175,176,177,178,],[14,14,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-79,-43,14,-16,-37,-42,14,-39,-36,-23,14,14,-40,-41,14,14,-38,14,-19,-21,-4,-20,14,14,-22,]),'ID':([0,3,4,6,7,8,9,10,11,14,15,16,17,18,19,20,28,30,32,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,68,69,78,79,81,82,83,101,107,110,111,112,113,117,120,122,123,125,131,141,144,145,148,150,152,153,159,160,161,162,164,166,168,174,175,176,177,178,],[15,15,-6,-8,-9,-10,-11,-12,-13,62,63,-17,-18,71,71,71,63,71,63,-80,-5,-7,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,-14,-15,71,71,71,108,-79,-43,63,71,15,71,-16,71,63,71,-37,-42,15,71,71,-39,71,147,-36,157,-23,15,15,-40,-41,15,71,15,-38,15,-19,-21,-4,-20,15,15,-22,]),'MINUS':([0,3,4,5,6,7,8,9,10,11,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,36,37,38,39,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,65,67,69,70,71,73,74,77,78,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,104,106,107,109,111,112,113,116,117,118,119,120,121,122,123,125,126,127,136,139,141,145,148,150,152,153,159,160,161,162,164,166,167,168,173,174,175,176,177,178,],[19,19,-6,44,-8,-9,-10,-11,-12,-13,-81,-17,-18,19,19,19,-63,-64,-65,-66,-67,-68,-69,-71,19,-72,-73,-74,-75,-5,-7,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-14,-15,-81,19,19,19,-79,44,-81,-57,-60,44,-43,19,19,19,-44,-45,-46,-47,-48,-49,-50,44,44,44,44,44,44,44,44,44,44,-16,44,44,44,19,-70,19,-37,-42,44,19,44,-32,19,-78,19,-39,19,-76,44,44,44,-36,-23,19,19,-40,-41,19,19,19,-38,19,-19,44,-21,-77,-4,-20,19,19,-22,]),'LNOT':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,30,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,69,78,81,82,83,101,107,111,112,113,117,120,122,123,125,141,145,148,150,152,153,159,160,161,162,164,166,168,174,175,176,177,178,],[20,20,-6,-8,-9,-10,-11,-12,-13,-17,-18,20,20,20,20,-5,-7,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-14,-15,20,20,20,-79,-43,20,20,20,-16,20,20,-37,-42,20,20,20,-39,20,-36,-23,20,20,-40,-41,20,20,20,-38,20,-19,-21,-4,-20,20,20,-22,]),'NULL':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,30,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,69,78,81,82,83,101,107,111,112,113,117,120,122,123,125,141,145,148,150,152,153,159,160,161,162,164,166,168,174,175,176,177,178,],[27,27,-6,-8,-9,-10,-11,-12,-13,-17,-18,27,27,27,27,-5,-7,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-14,-15,27,27,27,-79,-43,27,27,27,-16,27,27,-37,-42,27,27,27,-39,27,-36,-23,27,27,-40,-41,27,27,27,-38,27,-19,-21,-4,-20,27,27,-22,]),'LPAREN':([0,3,4,6,7,8,9,10,11,15,16,17,18,19,20,30,33,35,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,63,64,65,67,69,71,78,81,82,83,101,107,111,112,113,114,117,120,122,123,125,141,145,148,149,150,152,153,159,160,161,162,164,166,168,174,175,176,177,178,],[18,18,-6,-8,-9,-10,-11,-12,-13,64,-17,-18,18,18,18,18,81,83,-5,-7,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-14,-15,-81,18,18,18,-79,64,-43,18,18,18,-16,18,18,-37,-42,128,18,18,18,-39,18,-36,-23,18,160,18,-40,-41,18,18,18,-38,18,-19,-21,-4,-20,18,18,-22,]),'RETURN':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,82,101,112,113,117,123,141,145,148,150,152,153,159,161,162,164,166,168,174,175,176,177,178,],[30,30,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-79,-43,30,-16,-37,-42,30,-39,-36,-23,30,30,-40,-41,30,30,-38,30,-19,-21,-4,-20,30,30,-22,]),'FUNCTION':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,82,101,112,113,115,117,123,141,145,146,148,150,152,153,159,161,162,164,166,168,174,175,176,177,178,],[31,31,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-79,-43,31,-16,-37,-42,31,31,-39,-36,-23,31,31,31,-40,-41,31,31,-38,31,-19,-21,-4,-20,31,31,-22,]),'STRUCTURE':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,82,101,112,113,117,123,141,145,148,150,152,153,159,161,162,164,166,168,174,175,176,177,178,],[32,32,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-79,-43,32,-16,-37,-42,32,-39,-36,-23,32,32,-40,-41,32,32,-38,32,-19,-21,-4,-20,32,32,-22,]),'WHILE':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,82,101,112,113,117,123,134,141,145,148,150,152,153,159,161,162,164,166,168,174,175,176,177,178,],[33,33,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-79,-43,33,-16,-37,-42,33,-39,149,-36,-23,33,33,-40,-41,33,33,-38,33,-19,-21,-4,-20,33,33,-22,]),'DO':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,82,101,112,113,117,123,141,145,148,150,152,153,159,161,162,164,166,168,174,175,176,177,178,],[34,34,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-79,-43,34,-16,-37,-42,34,-39,-36,-23,34,34,-40,-41,34,34,-38,34,-19,-21,-4,-20,34,34,-22,]),'IF':([0,3,4,6,7,8,9,10,11,16,17,41,42,60,61,69,78,82,101,112,113,117,123,141,145,148,150,152,153,159,161,162,164,166,168,174,175,176,177,178,],[35,35,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-79,-43,35,-16,-37,-42,35,-39,-36,-23,35,35,-40,-41,35,35,-38,35,-19,-21,-4,-20,35,35,-22,]),'INTEGER':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,30,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,69,78,81,82,83,101,107,111,112,113,117,120,122,123,125,141,145,148,150,152,153,159,160,161,162,163,164,166,168,174,175,176,177,178,],[29,29,-6,-8,-9,-10,-11,-12,-13,-17,-18,29,29,29,29,-5,-7,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-14,-15,29,29,29,-79,-43,29,29,29,-16,29,29,-37,-42,29,29,29,-39,29,-36,-23,29,29,-40,-41,29,29,29,-38,169,29,-19,-21,-4,-20,29,29,-22,]),'DOUBLE':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,30,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,69,78,81,82,83,101,107,111,112,113,117,120,122,123,125,141,145,148,150,152,153,159,160,161,162,164,166,168,174,175,176,177,178,],[36,36,-6,-8,-9,-10,-11,-12,-13,-17,-18,36,36,36,36,-5,-7,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-14,-15,36,36,36,-79,-43,36,36,36,-16,36,36,-37,-42,36,36,36,-39,36,-36,-23,36,36,-40,-41,36,36,36,-38,36,-19,-21,-4,-20,36,36,-22,]),'BOOL':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,30,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,69,78,81,82,83,101,107,111,112,113,117,120,122,123,125,141,145,148,150,152,153,159,160,161,162,164,166,168,174,175,176,177,178,],[37,37,-6,-8,-9,-10,-11,-12,-13,-17,-18,37,37,37,37,-5,-7,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-14,-15,37,37,37,-79,-43,37,37,37,-16,37,37,-37,-42,37,37,37,-39,37,-36,-23,37,37,-40,-41,37,37,37,-38,37,-19,-21,-4,-20,37,37,-22,]),'STRING':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,30,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,69,78,81,82,83,101,107,111,112,113,117,120,122,123,125,141,145,148,150,152,153,159,160,161,162,164,166,168,174,175,176,177,178,],[38,38,-6,-8,-9,-10,-11,-12,-13,-17,-18,38,38,38,38,-5,-7,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-14,-15,38,38,38,-79,-43,38,38,38,-16,38,38,-37,-42,38,38,38,-39,38,-36,-23,38,38,-40,-41,38,38,38,-38,38,-19,-21,-4,-20,38,38,-22,]),'VOID':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,30,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,69,78,81,82,83,101,107,111,112,113,117,120,122,123,125,141,145,148,150,152,153,159,160,161,162,164,166,168,174,175,176,177,178,],[39,39,-6,-8,-9,-10,-11,-12,-13,-17,-18,39,39,39,39,-5,-7,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-14,-15,39,39,39,-79,-43,39,39,39,-16,39,39,-37,-42,39,39,39,-39,39,-36,-23,39,39,-40,-41,39,39,39,-38,39,-19,-21,-4,-20,39,39,-22,]),'DATATYPE':([0,3,4,6,7,8,9,10,11,16,17,18,19,20,30,31,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,67,69,78,81,82,83,101,107,111,112,113,115,117,120,122,123,125,128,140,141,145,146,148,150,152,153,156,159,160,161,162,164,166,168,174,175,176,177,178,],[40,40,-6,-8,-9,-10,-11,-12,-13,-17,-18,40,40,40,40,40,-5,-7,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-14,-15,40,40,40,-79,-43,40,40,40,-16,40,40,-37,-42,131,40,40,40,-39,40,144,40,-36,-23,131,40,40,-40,-41,144,40,40,40,-38,40,-19,-21,-4,-20,40,40,-22,]),'RBRACE':([3,4,6,7,8,9,10,11,16,17,21,22,23,24,25,26,27,29,36,37,38,39,41,42,60,61,63,69,71,73,74,78,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,107,109,112,113,117,119,121,122,123,124,126,129,130,132,136,137,141,145,147,152,153,158,159,161,162,166,168,170,173,174,175,177,178,],[-3,-6,-8,-9,-10,-11,-12,-13,-17,-18,-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-5,-7,-14,-15,-81,-79,-81,-57,-60,-43,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,-59,-61,-62,-16,-34,-33,-70,-37,-42,134,-32,-78,-33,-39,138,-76,145,-24,-27,-35,151,-36,-23,-26,-40,-41,-25,166,168,-38,-19,-21,174,-77,-4,-20,178,-22,]),'SEMI':([5,12,13,15,21,22,23,24,25,26,27,29,30,36,37,38,39,62,63,71,73,74,76,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,106,109,119,121,126,127,138,139,151,171,173,],[42,60,61,-81,-63,-64,-65,-66,-67,-68,-69,-71,78,-72,-73,-74,-75,101,-81,-81,-57,-60,112,113,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,-59,-61,-62,123,-70,-32,-78,-76,141,152,153,162,175,-77,]),'PLUS':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,106,109,116,118,119,121,126,127,136,139,167,173,],[43,-81,-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,43,-81,-57,-60,43,-44,-45,-46,-47,-48,-49,-50,43,43,43,43,43,43,43,43,43,43,43,43,43,-70,43,43,-32,-78,-76,43,43,43,43,-77,]),'MUL':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,106,109,116,118,119,121,126,127,136,139,167,173,],[45,-81,-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,45,-81,-57,-60,45,45,45,-46,-47,-48,-49,-50,45,45,45,45,45,45,45,45,45,45,45,45,45,-70,45,45,-32,-78,-76,45,45,45,45,-77,]),'DIVIDE':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,106,109,116,118,119,121,126,127,136,139,167,173,],[46,-81,-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,46,-81,-57,-60,46,46,46,-46,-47,-48,-49,-50,46,46,46,46,46,46,46,46,46,46,46,46,46,-70,46,46,-32,-78,-76,46,46,46,46,-77,]),'INTDIVIDE':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,106,109,116,118,119,121,126,127,136,139,167,173,],[47,-81,-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,47,-81,-57,-60,47,47,47,-46,-47,-48,-49,-50,47,47,47,47,47,47,47,47,47,47,47,47,47,-70,47,47,-32,-78,-76,47,47,47,47,-77,]),'MODULO':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,106,109,116,118,119,121,126,127,136,139,167,173,],[48,-81,-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,48,-81,-57,-60,48,48,48,-46,-47,-48,-49,-50,48,48,48,48,48,48,48,48,48,48,48,48,48,-70,48,48,-32,-78,-76,48,48,48,48,-77,]),'POW':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,106,109,116,118,119,121,126,127,136,139,167,173,],[49,-81,-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,49,-81,-57,-60,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-70,49,49,-32,-78,-76,49,49,49,49,-77,]),'LE':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,106,109,116,118,119,121,126,127,136,139,167,173,],[50,-81,-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,50,-81,-57,-60,50,-44,-45,-46,-47,-48,-49,-50,None,None,None,None,50,50,50,50,50,50,50,50,50,-70,50,50,-32,-78,-76,50,50,50,50,-77,]),'GE':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,106,109,116,118,119,121,126,127,136,139,167,173,],[51,-81,-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,51,-81,-57,-60,51,-44,-45,-46,-47,-48,-49,-50,None,None,None,None,51,51,51,51,51,51,51,51,51,-70,51,51,-32,-78,-76,51,51,51,51,-77,]),'LT':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,106,109,116,118,119,121,126,127,136,139,167,173,],[52,-81,-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,52,-81,-57,-60,52,-44,-45,-46,-47,-48,-49,-50,None,None,None,None,52,52,52,52,52,52,52,52,52,-70,52,52,-32,-78,-76,52,52,52,52,-77,]),'GT':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,106,109,116,118,119,121,126,127,136,139,167,173,],[53,-81,-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,53,-81,-57,-60,53,-44,-45,-46,-47,-48,-49,-50,None,None,None,None,53,53,53,53,53,53,53,53,53,-70,53,53,-32,-78,-76,53,53,53,53,-77,]),'EQ':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,106,109,116,118,119,121,126,127,136,139,167,173,],[54,-81,-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,54,-81,-57,-60,54,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,None,None,54,54,54,54,54,54,54,-70,54,54,-32,-78,-76,54,54,54,54,-77,]),'NE':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,106,109,116,118,119,121,126,127,136,139,167,173,],[55,-81,-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,55,-81,-57,-60,55,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,None,None,55,55,55,55,55,55,55,-70,55,55,-32,-78,-76,55,55,55,55,-77,]),'LAND':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,106,109,116,118,119,121,126,127,136,139,167,173,],[56,-81,-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,56,-81,-57,-60,56,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,None,56,-61,-62,56,56,56,-70,56,56,-32,-78,-76,56,56,56,56,-77,]),'LOR':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,106,109,116,118,119,121,126,127,136,139,167,173,],[57,-81,-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,57,-81,-57,-60,57,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,None,-61,-62,57,57,57,-70,57,57,-32,-78,-76,57,57,57,57,-77,]),'BAND':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,106,109,116,118,119,121,126,127,136,139,167,173,],[58,-81,-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,58,-81,-57,-60,58,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,58,58,None,58,58,58,58,-70,58,58,-32,-78,-76,58,58,58,58,-77,]),'BOR':([5,15,21,22,23,24,25,26,27,29,36,37,38,39,63,70,71,73,74,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,106,109,116,118,119,121,126,127,136,139,167,173,],[59,-81,-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,59,-81,-57,-60,59,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,59,59,-61,None,59,59,59,-70,59,59,-32,-78,-76,59,59,59,59,-77,]),'LBRACKET':([15,28,40,71,72,154,],[65,75,-80,65,75,163,]),'EQUALS':([15,63,66,76,108,126,],[67,-81,105,111,125,140,]),'DOT':([15,],[68,]),'COLON':([15,],[69,]),'RPAREN':([21,22,23,24,25,26,27,29,36,37,38,39,63,64,70,71,73,74,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,109,116,118,119,121,126,128,136,142,143,157,165,167,173,],[-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,-33,109,-81,-57,-60,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,-59,-61,-62,119,-34,-70,133,135,-32,-78,-76,-28,-35,155,-29,-31,-30,171,-77,]),'COMMA':([21,22,23,24,25,26,27,29,36,37,38,39,63,64,71,73,74,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,102,103,107,109,119,121,122,124,126,128,129,130,132,136,137,142,143,147,157,158,165,173,174,],[-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,-33,-81,-57,-60,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,-59,-61,-62,120,-34,-33,-70,-32,-78,-33,120,-76,-28,146,-24,-27,-35,120,156,-29,-26,-31,-25,-30,-77,-4,]),'RBRACKET':([21,22,23,24,25,26,27,29,36,37,38,39,63,71,73,74,75,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,104,109,119,121,126,169,173,],[-63,-64,-65,-66,-67,-68,-69,-71,-72,-73,-74,-75,-81,-81,-57,-60,110,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-58,-59,-61,-62,121,-70,-32,-78,-76,173,-77,]),'LBRACE':([34,63,67,80,105,133,135,155,172,],[82,-81,107,115,122,148,150,164,176,]),'ELSE':([168,],[172,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'basic_block':([0,164,],[2,170,]),'stmt_list':([0,82,148,150,164,176,],[3,117,159,161,3,177,]),'statement':([0,3,82,117,148,150,159,161,164,176,177,],[4,41,4,41,4,4,41,41,4,4,41,]),'expr':([0,3,18,19,20,30,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,64,65,67,81,82,83,107,111,117,120,122,125,148,150,159,160,161,164,176,177,],[5,5,70,73,74,77,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,103,104,106,116,5,118,103,127,5,136,103,139,5,5,5,167,5,5,5,5,]),'var_declaration':([0,3,82,117,148,150,159,161,164,176,177,],[6,6,6,6,6,6,6,6,6,6,6,]),'return':([0,3,82,117,148,150,159,161,164,176,177,],[7,7,7,7,7,7,7,7,7,7,7,]),'assign':([0,3,82,117,148,150,159,161,164,176,177,],[8,8,8,8,8,8,8,8,8,8,8,]),'func_declaration':([0,3,82,115,117,146,148,150,159,161,164,176,177,],[9,9,9,132,9,132,9,9,9,9,9,9,9,]),'struct_declaration':([0,3,82,117,148,150,159,161,164,176,177,],[10,10,10,10,10,10,10,10,10,10,10,]),'while':([0,3,82,117,148,150,159,161,164,176,177,],[11,11,11,11,11,11,11,11,11,11,11,]),'goto_mark':([0,3,82,117,148,150,159,161,164,176,177,],[16,16,16,16,16,16,16,16,16,16,16,]),'if-else':([0,3,82,117,148,150,159,161,164,176,177,],[17,17,17,17,17,17,17,17,17,17,17,]),'id':([0,3,15,18,19,20,28,30,32,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,64,65,67,79,81,82,83,107,110,111,117,120,122,125,148,150,159,160,161,164,176,177,],[21,21,66,21,21,21,76,21,80,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,114,21,21,21,21,126,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'int':([0,3,18,19,20,30,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,64,65,67,81,82,83,107,111,117,120,122,125,148,150,159,160,161,164,176,177,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'double':([0,3,18,19,20,30,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,64,65,67,81,82,83,107,111,117,120,122,125,148,150,159,160,161,164,176,177,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'bool':([0,3,18,19,20,30,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,64,65,67,81,82,83,107,111,117,120,122,125,148,150,159,160,161,164,176,177,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'str':([0,3,18,19,20,30,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,64,65,67,81,82,83,107,111,117,120,122,125,148,150,159,160,161,164,176,177,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'void':([0,3,18,19,20,30,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,64,65,67,81,82,83,107,111,117,120,122,125,148,150,159,160,161,164,176,177,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'datatype':([0,3,18,19,20,30,31,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,64,65,67,81,82,83,107,111,117,120,122,125,140,148,150,159,160,161,164,176,177,],[28,28,72,72,72,72,79,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,28,72,72,72,28,72,72,72,154,28,28,28,72,28,28,28,28,]),'args':([64,107,122,],[102,124,137,]),'struct_params':([115,],[129,]),'struct_param':([115,146,],[130,158,]),'params':([128,],[142,]),'param':([128,156,],[143,165,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> <empty>','program',0,'p_program','doh_parser.py',34),
  ('program -> basic_block','program',1,'p_program','doh_parser.py',35),
  ('basic_block -> stmt_list','basic_block',1,'p_basic_block','doh_parser.py',43),
  ('func_declaration -> FUNCTION datatype id LPAREN params RPAREN LBRACE basic_block RBRACE','func_declaration',9,'p_func_declaration','doh_parser.py',48),
  ('stmt_list -> stmt_list statement','stmt_list',2,'p_stmt_list','doh_parser.py',53),
  ('stmt_list -> statement','stmt_list',1,'p_stmt_list','doh_parser.py',54),
  ('statement -> expr SEMI','statement',2,'p_stmt','doh_parser.py',63),
  ('statement -> var_declaration','statement',1,'p_stmt','doh_parser.py',64),
  ('statement -> return','statement',1,'p_stmt','doh_parser.py',65),
  ('statement -> assign','statement',1,'p_stmt','doh_parser.py',66),
  ('statement -> func_declaration','statement',1,'p_stmt','doh_parser.py',67),
  ('statement -> struct_declaration','statement',1,'p_stmt','doh_parser.py',68),
  ('statement -> while','statement',1,'p_stmt','doh_parser.py',69),
  ('statement -> BREAK SEMI','statement',2,'p_stmt','doh_parser.py',70),
  ('statement -> CONTINUE SEMI','statement',2,'p_stmt','doh_parser.py',71),
  ('statement -> GOTO ID SEMI','statement',3,'p_stmt','doh_parser.py',72),
  ('statement -> goto_mark','statement',1,'p_stmt','doh_parser.py',73),
  ('statement -> if-else','statement',1,'p_stmt','doh_parser.py',74),
  ('while -> WHILE LPAREN expr RPAREN LBRACE stmt_list RBRACE','while',7,'p_loops','doh_parser.py',88),
  ('while -> DO LBRACE stmt_list RBRACE WHILE LPAREN expr RPAREN SEMI','while',9,'p_loops','doh_parser.py',89),
  ('if-else -> IF LPAREN expr RPAREN LBRACE stmt_list RBRACE','if-else',7,'p_if_else','doh_parser.py',99),
  ('if-else -> IF LPAREN expr RPAREN LBRACE stmt_list RBRACE ELSE LBRACE stmt_list RBRACE','if-else',11,'p_if_else','doh_parser.py',100),
  ('struct_declaration -> STRUCTURE id LBRACE struct_params RBRACE','struct_declaration',5,'p_struct_declaration','doh_parser.py',110),
  ('struct_params -> struct_param','struct_params',1,'p_struct_params','doh_parser.py',117),
  ('struct_params -> struct_params COMMA struct_param','struct_params',3,'p_struct_params','doh_parser.py',118),
  ('struct_param -> DATATYPE ID','struct_param',2,'p_struct_param','doh_parser.py',128),
  ('struct_param -> func_declaration','struct_param',1,'p_struct_param','doh_parser.py',129),
  ('params -> <empty>','params',0,'p_params','doh_parser.py',138),
  ('params -> param','params',1,'p_params','doh_parser.py',139),
  ('params -> params COMMA param','params',3,'p_params','doh_parser.py',140),
  ('param -> DATATYPE ID','param',2,'p_param_declaration','doh_parser.py',150),
  ('expr -> ID LPAREN args RPAREN','expr',4,'p_func_call','doh_parser.py',155),
  ('args -> <empty>','args',0,'p_arguments','doh_parser.py',160),
  ('args -> expr','args',1,'p_arguments','doh_parser.py',161),
  ('args -> args COMMA expr','args',3,'p_arguments','doh_parser.py',162),
  ('var_declaration -> datatype id EQUALS expr SEMI','var_declaration',5,'p_var_declaration','doh_parser.py',174),
  ('var_declaration -> datatype id SEMI','var_declaration',3,'p_var_declaration','doh_parser.py',175),
  ('var_declaration -> ID id EQUALS LBRACE args RBRACE SEMI','var_declaration',7,'p_var_declaration','doh_parser.py',176),
  ('assign -> ID EQUALS expr SEMI','assign',4,'p_assign','doh_parser.py',188),
  ('assign -> ID EQUALS LBRACE args RBRACE SEMI','assign',6,'p_assign','doh_parser.py',189),
  ('assign -> ID DOT ID EQUALS expr SEMI','assign',6,'p_assign','doh_parser.py',190),
  ('return -> RETURN expr SEMI','return',3,'p_return','doh_parser.py',201),
  ('return -> RETURN SEMI','return',2,'p_return','doh_parser.py',202),
  ('expr -> expr PLUS expr','expr',3,'p_math_expressions','doh_parser.py',211),
  ('expr -> expr MINUS expr','expr',3,'p_math_expressions','doh_parser.py',212),
  ('expr -> expr MUL expr','expr',3,'p_math_expressions','doh_parser.py',213),
  ('expr -> expr DIVIDE expr','expr',3,'p_math_expressions','doh_parser.py',214),
  ('expr -> expr INTDIVIDE expr','expr',3,'p_math_expressions','doh_parser.py',215),
  ('expr -> expr MODULO expr','expr',3,'p_math_expressions','doh_parser.py',216),
  ('expr -> expr POW expr','expr',3,'p_math_expressions','doh_parser.py',217),
  ('expr -> expr LE expr','expr',3,'p_conditionals','doh_parser.py',238),
  ('expr -> expr GE expr','expr',3,'p_conditionals','doh_parser.py',239),
  ('expr -> expr LT expr','expr',3,'p_conditionals','doh_parser.py',240),
  ('expr -> expr GT expr','expr',3,'p_conditionals','doh_parser.py',241),
  ('expr -> expr EQ expr','expr',3,'p_conditionals','doh_parser.py',242),
  ('expr -> expr NE expr','expr',3,'p_conditionals','doh_parser.py',243),
  ('expr -> MINUS expr','expr',2,'p_logical_operation','doh_parser.py',259),
  ('expr -> expr LAND expr','expr',3,'p_logical_operation','doh_parser.py',260),
  ('expr -> expr LOR expr','expr',3,'p_logical_operation','doh_parser.py',261),
  ('expr -> LNOT expr','expr',2,'p_logical_operation','doh_parser.py',262),
  ('expr -> expr BAND expr','expr',3,'p_bitwise_operation','doh_parser.py',275),
  ('expr -> expr BOR expr','expr',3,'p_bitwise_operation','doh_parser.py',276),
  ('expr -> id','expr',1,'p_literals','doh_parser.py',285),
  ('expr -> int','expr',1,'p_literals','doh_parser.py',286),
  ('expr -> double','expr',1,'p_literals','doh_parser.py',287),
  ('expr -> bool','expr',1,'p_literals','doh_parser.py',288),
  ('expr -> str','expr',1,'p_literals','doh_parser.py',289),
  ('expr -> void','expr',1,'p_literals','doh_parser.py',290),
  ('expr -> NULL','expr',1,'p_literals','doh_parser.py',291),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_literals','doh_parser.py',292),
  ('int -> INTEGER','int',1,'p_const_int','doh_parser.py',300),
  ('double -> DOUBLE','double',1,'p_const_double','doh_parser.py',305),
  ('bool -> BOOL','bool',1,'p_const_bool','doh_parser.py',310),
  ('str -> STRING','str',1,'p_const_string','doh_parser.py',315),
  ('void -> VOID','void',1,'p_void','doh_parser.py',320),
  ('expr -> datatype LBRACKET RBRACKET id','expr',4,'p_array_init','doh_parser.py',326),
  ('expr -> datatype LBRACKET RBRACKET id EQUALS datatype LBRACKET INTEGER RBRACKET','expr',9,'p_array_init','doh_parser.py',327),
  ('expr -> ID LBRACKET expr RBRACKET','expr',4,'p_index','doh_parser.py',336),
  ('goto_mark -> ID COLON','goto_mark',2,'p_goto_mark','doh_parser.py',341),
  ('datatype -> DATATYPE','datatype',1,'p_datatype','doh_parser.py',346),
  ('id -> ID','id',1,'p_id','doh_parser.py',351),
]

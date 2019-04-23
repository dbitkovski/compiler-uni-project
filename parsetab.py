
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftCOMMArightEQUALSnonassocLORnonassocLANDnonassocBORnonassocBANDnonassocEQNEnonassocLEGELTGTleftPLUSMINUSleftMULDIVIDEINTDIVIDEMODULOrightPOWrightUMINUSLNOTleftLBRACERBRACELPARENRPARENLBRACKETRBRACKETBAND BOOL BOR BREAK COLON COMMA COMMENT CONTINUE DATATYPE DIVIDE DO DOT DOUBLE ELSE EQ EQUALS ERROR FUNCTION GE GOTO GT ID IF INTDIVIDE INTEGER LAND LBRACE LBRACKET LE LNOT LOR LPAREN LT MINUS MODULO MUL NE NEWLINE NULL PLUS POW RBRACE RBRACKET RETURN RPAREN SEMI STRING STRUCTURE VOID WHILEprogram :\n               | scope\n    basic_block : LBRACE scope RBRACE\n    func_declaration : FUNCTION datatype id LPAREN params RPAREN basic_blockscope : scope statement\n             | statement\n    statement : expr SEMI\n              | var_declaration\n              | return\n              | assign\n              | func_declaration\n              | struct_declaration\n              | while\n              | BREAK SEMI\n              | CONTINUE SEMI\n              | GOTO ID SEMI\n              | goto_mark\n              | if-else\n    \n    while : WHILE conditional basic_block\n          | DO basic_block WHILE conditional SEMI\n    \n    if-else : IF conditional basic_block\n            | IF conditional basic_block ELSE basic_block\n    conditional : LPAREN expr RPAREN\n    struct_declaration : STRUCTURE id LBRACE struct_params RBRACE\n    \n    struct_params : struct_param\n                  | struct_params COMMA struct_param\n    \n    struct_param : DATATYPE ID\n                 | func_declaration\n    params :\n              | param\n              | params COMMA paramparam : DATATYPE IDexpr : ID LPAREN args RPARENargs :\n            | expr\n            | args COMMA expr\n    var_declaration : datatype id EQUALS expr SEMI\n                    | datatype id SEMI\n                    | ID id EQUALS LBRACE args RBRACE SEMI\n    assign : ID EQUALS expr SEMI\n              | ID EQUALS LBRACE args RBRACE SEMI\n              | ID DOT ID EQUALS expr SEMI\n    return : RETURN expr SEMI\n           | RETURN SEMI\n    expr : expr PLUS expr\n            | expr MINUS expr\n            | expr MUL expr\n            | expr DIVIDE expr\n            | expr INTDIVIDE expr\n            | expr MODULO expr\n            | expr POW exprexpr : expr LE expr\n            | expr GE expr\n            | expr LT expr\n            | expr GT expr\n            | expr EQ expr\n            | expr NE exprexpr : MINUS expr %prec UMINUS\n            | expr LAND expr\n            | expr LOR expr\n            | LNOT expr\n    expr : expr BAND expr\n         | expr BOR expr\n    expr : id\n            | int\n            | double\n            | bool\n            | str\n            | void\n            | NULL\n            | LPAREN expr RPARENint : INTEGERdouble : DOUBLEbool : BOOLstr : STRINGvoid : VOID\n    expr : datatype LBRACKET RBRACKET id\n         | datatype LBRACKET RBRACKET id EQUALS datatype LBRACKET INTEGER RBRACKET\n    expr : ID LBRACKET expr RBRACKETgoto_mark : ID COLONdatatype : DATATYPEid : ID'
    
_lr_action_items = {'$end':([0,1,2,3,5,6,7,8,9,10,15,16,40,41,59,60,68,77,102,113,114,117,121,126,138,145,149,152,153,155,156,162,164,],[-1,0,-2,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-80,-44,-16,-38,-43,-19,-21,-40,-3,-37,-24,-20,-22,-41,-42,-39,-4,]),'BREAK':([0,2,3,5,6,7,8,9,10,15,16,40,41,59,60,68,77,83,102,113,114,117,120,121,126,138,145,149,152,153,155,156,162,164,],[11,11,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-80,-44,11,-16,-38,-43,-19,11,-21,-40,-3,-37,-24,-20,-22,-41,-42,-39,-4,]),'CONTINUE':([0,2,3,5,6,7,8,9,10,15,16,40,41,59,60,68,77,83,102,113,114,117,120,121,126,138,145,149,152,153,155,156,162,164,],[12,12,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-80,-44,12,-16,-38,-43,-19,12,-21,-40,-3,-37,-24,-20,-22,-41,-42,-39,-4,]),'GOTO':([0,2,3,5,6,7,8,9,10,15,16,40,41,59,60,68,77,83,102,113,114,117,120,121,126,138,145,149,152,153,155,156,162,164,],[13,13,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-80,-44,13,-16,-38,-43,-19,13,-21,-40,-3,-37,-24,-20,-22,-41,-42,-39,-4,]),'ID':([0,2,3,5,6,7,8,9,10,13,14,15,16,17,18,19,27,29,31,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,63,64,66,67,68,77,78,81,83,102,108,111,112,113,114,117,120,121,123,125,126,128,134,138,145,148,149,152,153,155,156,162,164,],[14,14,-6,-8,-9,-10,-11,-12,-13,61,62,-17,-18,70,70,70,62,70,62,-81,-5,-7,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,-14,-15,70,70,70,109,-80,-44,62,70,14,-16,70,62,70,-38,-43,-19,14,-21,70,70,-40,70,151,-3,-37,160,-24,-20,-22,-41,-42,-39,-4,]),'MINUS':([0,2,3,4,5,6,7,8,9,10,14,15,16,17,18,19,20,21,22,23,24,25,26,28,29,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,66,68,69,70,72,73,76,77,81,83,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,105,107,108,110,112,113,114,117,118,120,121,122,123,124,125,126,128,129,130,138,140,143,145,149,152,153,155,156,162,164,167,],[18,18,-6,43,-8,-9,-10,-11,-12,-13,-82,-17,-18,18,18,18,-64,-65,-66,-67,-68,-69,-70,-72,18,-73,-74,-75,-76,-5,-7,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-14,-15,-82,18,18,18,-80,43,-82,-58,-61,43,-44,18,18,-45,-46,-47,-48,-49,-50,-51,43,43,43,43,43,43,43,43,43,43,-16,43,43,43,18,-71,18,-38,-43,-19,43,18,-21,-33,18,-79,18,-40,18,-77,43,-3,43,43,-37,-24,-20,-22,-41,-42,-39,-4,-78,]),'LNOT':([0,2,3,5,6,7,8,9,10,15,16,17,18,19,29,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,63,64,66,68,77,81,83,102,108,112,113,114,117,120,121,123,125,126,128,138,145,149,152,153,155,156,162,164,],[19,19,-6,-8,-9,-10,-11,-12,-13,-17,-18,19,19,19,19,-5,-7,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-14,-15,19,19,19,-80,-44,19,19,-16,19,19,-38,-43,-19,19,-21,19,19,-40,19,-3,-37,-24,-20,-22,-41,-42,-39,-4,]),'NULL':([0,2,3,5,6,7,8,9,10,15,16,17,18,19,29,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,63,64,66,68,77,81,83,102,108,112,113,114,117,120,121,123,125,126,128,138,145,149,152,153,155,156,162,164,],[26,26,-6,-8,-9,-10,-11,-12,-13,-17,-18,26,26,26,26,-5,-7,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-14,-15,26,26,26,-80,-44,26,26,-16,26,26,-38,-43,-19,26,-21,26,26,-40,26,-3,-37,-24,-20,-22,-41,-42,-39,-4,]),'LPAREN':([0,2,3,5,6,7,8,9,10,14,15,16,17,18,19,29,32,34,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,62,63,64,66,68,70,77,81,83,102,108,112,113,114,115,117,119,120,121,123,125,126,128,138,145,149,152,153,155,156,162,164,],[17,17,-6,-8,-9,-10,-11,-12,-13,63,-17,-18,17,17,17,17,81,81,-5,-7,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-14,-15,-82,17,17,17,-80,63,-44,17,17,-16,17,17,-38,-43,131,-19,81,17,-21,17,17,-40,17,-3,-37,-24,-20,-22,-41,-42,-39,-4,]),'RETURN':([0,2,3,5,6,7,8,9,10,15,16,40,41,59,60,68,77,83,102,113,114,117,120,121,126,138,145,149,152,153,155,156,162,164,],[29,29,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-80,-44,29,-16,-38,-43,-19,29,-21,-40,-3,-37,-24,-20,-22,-41,-42,-39,-4,]),'FUNCTION':([0,2,3,5,6,7,8,9,10,15,16,40,41,59,60,68,77,83,102,113,114,116,117,120,121,126,138,145,149,150,152,153,155,156,162,164,],[30,30,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-80,-44,30,-16,-38,-43,30,-19,30,-21,-40,-3,-37,-24,30,-20,-22,-41,-42,-39,-4,]),'STRUCTURE':([0,2,3,5,6,7,8,9,10,15,16,40,41,59,60,68,77,83,102,113,114,117,120,121,126,138,145,149,152,153,155,156,162,164,],[31,31,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-80,-44,31,-16,-38,-43,-19,31,-21,-40,-3,-37,-24,-20,-22,-41,-42,-39,-4,]),'WHILE':([0,2,3,5,6,7,8,9,10,15,16,40,41,59,60,68,77,82,83,102,113,114,117,120,121,126,138,145,149,152,153,155,156,162,164,],[32,32,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-80,-44,119,32,-16,-38,-43,-19,32,-21,-40,-3,-37,-24,-20,-22,-41,-42,-39,-4,]),'DO':([0,2,3,5,6,7,8,9,10,15,16,40,41,59,60,68,77,83,102,113,114,117,120,121,126,138,145,149,152,153,155,156,162,164,],[33,33,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-80,-44,33,-16,-38,-43,-19,33,-21,-40,-3,-37,-24,-20,-22,-41,-42,-39,-4,]),'IF':([0,2,3,5,6,7,8,9,10,15,16,40,41,59,60,68,77,83,102,113,114,117,120,121,126,138,145,149,152,153,155,156,162,164,],[34,34,-6,-8,-9,-10,-11,-12,-13,-17,-18,-5,-7,-14,-15,-80,-44,34,-16,-38,-43,-19,34,-21,-40,-3,-37,-24,-20,-22,-41,-42,-39,-4,]),'INTEGER':([0,2,3,5,6,7,8,9,10,15,16,17,18,19,29,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,63,64,66,68,77,81,83,102,108,112,113,114,117,120,121,123,125,126,128,138,145,149,152,153,155,156,162,163,164,],[28,28,-6,-8,-9,-10,-11,-12,-13,-17,-18,28,28,28,28,-5,-7,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-14,-15,28,28,28,-80,-44,28,28,-16,28,28,-38,-43,-19,28,-21,28,28,-40,28,-3,-37,-24,-20,-22,-41,-42,-39,166,-4,]),'DOUBLE':([0,2,3,5,6,7,8,9,10,15,16,17,18,19,29,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,63,64,66,68,77,81,83,102,108,112,113,114,117,120,121,123,125,126,128,138,145,149,152,153,155,156,162,164,],[35,35,-6,-8,-9,-10,-11,-12,-13,-17,-18,35,35,35,35,-5,-7,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-14,-15,35,35,35,-80,-44,35,35,-16,35,35,-38,-43,-19,35,-21,35,35,-40,35,-3,-37,-24,-20,-22,-41,-42,-39,-4,]),'BOOL':([0,2,3,5,6,7,8,9,10,15,16,17,18,19,29,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,63,64,66,68,77,81,83,102,108,112,113,114,117,120,121,123,125,126,128,138,145,149,152,153,155,156,162,164,],[36,36,-6,-8,-9,-10,-11,-12,-13,-17,-18,36,36,36,36,-5,-7,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-14,-15,36,36,36,-80,-44,36,36,-16,36,36,-38,-43,-19,36,-21,36,36,-40,36,-3,-37,-24,-20,-22,-41,-42,-39,-4,]),'STRING':([0,2,3,5,6,7,8,9,10,15,16,17,18,19,29,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,63,64,66,68,77,81,83,102,108,112,113,114,117,120,121,123,125,126,128,138,145,149,152,153,155,156,162,164,],[37,37,-6,-8,-9,-10,-11,-12,-13,-17,-18,37,37,37,37,-5,-7,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-14,-15,37,37,37,-80,-44,37,37,-16,37,37,-38,-43,-19,37,-21,37,37,-40,37,-3,-37,-24,-20,-22,-41,-42,-39,-4,]),'VOID':([0,2,3,5,6,7,8,9,10,15,16,17,18,19,29,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,63,64,66,68,77,81,83,102,108,112,113,114,117,120,121,123,125,126,128,138,145,149,152,153,155,156,162,164,],[38,38,-6,-8,-9,-10,-11,-12,-13,-17,-18,38,38,38,38,-5,-7,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,-14,-15,38,38,38,-80,-44,38,38,-16,38,38,-38,-43,-19,38,-21,38,38,-40,38,-3,-37,-24,-20,-22,-41,-42,-39,-4,]),'DATATYPE':([0,2,3,5,6,7,8,9,10,15,16,17,18,19,29,30,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,63,64,66,68,77,81,83,102,108,112,113,114,116,117,120,121,123,125,126,128,131,138,144,145,149,150,152,153,155,156,159,162,164,],[39,39,-6,-8,-9,-10,-11,-12,-13,-17,-18,39,39,39,39,39,-5,-7,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-14,-15,39,39,39,-80,-44,39,39,-16,39,39,-38,-43,134,-19,39,-21,39,39,-40,39,148,-3,39,-37,-24,134,-20,-22,-41,-42,148,-39,-4,]),'RBRACE':([3,5,6,7,8,9,10,15,16,20,21,22,23,24,25,26,28,35,36,37,38,40,41,59,60,62,68,70,72,73,77,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,108,110,113,114,117,120,121,122,124,125,126,127,129,132,133,135,138,140,141,145,149,151,152,153,155,156,161,162,164,167,],[-6,-8,-9,-10,-11,-12,-13,-17,-18,-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-5,-7,-14,-15,-82,-80,-82,-58,-61,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-59,-60,-62,-63,-16,-35,-34,-71,-38,-43,-19,138,-21,-33,-79,-34,-40,142,-77,149,-25,-28,-3,-36,154,-37,-24,-27,-20,-22,-41,-42,-26,-39,-4,-78,]),'SEMI':([4,11,12,14,20,21,22,23,24,25,26,28,29,35,36,37,38,61,62,70,72,73,75,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,107,110,122,124,129,130,136,137,142,143,154,167,],[41,59,60,-82,-64,-65,-66,-67,-68,-69,-70,-72,77,-73,-74,-75,-76,102,-82,-82,-58,-61,113,114,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-59,-60,-62,-63,126,-71,-33,-79,-77,145,-23,152,155,156,162,-78,]),'PLUS':([4,14,20,21,22,23,24,25,26,28,35,36,37,38,62,69,70,72,73,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,118,122,124,129,130,140,143,167,],[42,-82,-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,42,-82,-58,-61,42,-45,-46,-47,-48,-49,-50,-51,42,42,42,42,42,42,42,42,42,42,42,42,42,-71,42,-33,-79,-77,42,42,42,-78,]),'MUL':([4,14,20,21,22,23,24,25,26,28,35,36,37,38,62,69,70,72,73,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,118,122,124,129,130,140,143,167,],[44,-82,-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,44,-82,-58,-61,44,44,44,-47,-48,-49,-50,-51,44,44,44,44,44,44,44,44,44,44,44,44,44,-71,44,-33,-79,-77,44,44,44,-78,]),'DIVIDE':([4,14,20,21,22,23,24,25,26,28,35,36,37,38,62,69,70,72,73,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,118,122,124,129,130,140,143,167,],[45,-82,-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,45,-82,-58,-61,45,45,45,-47,-48,-49,-50,-51,45,45,45,45,45,45,45,45,45,45,45,45,45,-71,45,-33,-79,-77,45,45,45,-78,]),'INTDIVIDE':([4,14,20,21,22,23,24,25,26,28,35,36,37,38,62,69,70,72,73,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,118,122,124,129,130,140,143,167,],[46,-82,-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,46,-82,-58,-61,46,46,46,-47,-48,-49,-50,-51,46,46,46,46,46,46,46,46,46,46,46,46,46,-71,46,-33,-79,-77,46,46,46,-78,]),'MODULO':([4,14,20,21,22,23,24,25,26,28,35,36,37,38,62,69,70,72,73,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,118,122,124,129,130,140,143,167,],[47,-82,-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,47,-82,-58,-61,47,47,47,-47,-48,-49,-50,-51,47,47,47,47,47,47,47,47,47,47,47,47,47,-71,47,-33,-79,-77,47,47,47,-78,]),'POW':([4,14,20,21,22,23,24,25,26,28,35,36,37,38,62,69,70,72,73,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,118,122,124,129,130,140,143,167,],[48,-82,-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,48,-82,-58,-61,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-71,48,-33,-79,-77,48,48,48,-78,]),'LE':([4,14,20,21,22,23,24,25,26,28,35,36,37,38,62,69,70,72,73,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,118,122,124,129,130,140,143,167,],[49,-82,-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,49,-82,-58,-61,49,-45,-46,-47,-48,-49,-50,-51,None,None,None,None,49,49,49,49,49,49,49,49,49,-71,49,-33,-79,-77,49,49,49,-78,]),'GE':([4,14,20,21,22,23,24,25,26,28,35,36,37,38,62,69,70,72,73,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,118,122,124,129,130,140,143,167,],[50,-82,-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,50,-82,-58,-61,50,-45,-46,-47,-48,-49,-50,-51,None,None,None,None,50,50,50,50,50,50,50,50,50,-71,50,-33,-79,-77,50,50,50,-78,]),'LT':([4,14,20,21,22,23,24,25,26,28,35,36,37,38,62,69,70,72,73,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,118,122,124,129,130,140,143,167,],[51,-82,-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,51,-82,-58,-61,51,-45,-46,-47,-48,-49,-50,-51,None,None,None,None,51,51,51,51,51,51,51,51,51,-71,51,-33,-79,-77,51,51,51,-78,]),'GT':([4,14,20,21,22,23,24,25,26,28,35,36,37,38,62,69,70,72,73,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,118,122,124,129,130,140,143,167,],[52,-82,-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,52,-82,-58,-61,52,-45,-46,-47,-48,-49,-50,-51,None,None,None,None,52,52,52,52,52,52,52,52,52,-71,52,-33,-79,-77,52,52,52,-78,]),'EQ':([4,14,20,21,22,23,24,25,26,28,35,36,37,38,62,69,70,72,73,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,118,122,124,129,130,140,143,167,],[53,-82,-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,53,-82,-58,-61,53,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,None,None,53,53,53,53,53,53,53,-71,53,-33,-79,-77,53,53,53,-78,]),'NE':([4,14,20,21,22,23,24,25,26,28,35,36,37,38,62,69,70,72,73,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,118,122,124,129,130,140,143,167,],[54,-82,-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,54,-82,-58,-61,54,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,None,None,54,54,54,54,54,54,54,-71,54,-33,-79,-77,54,54,54,-78,]),'LAND':([4,14,20,21,22,23,24,25,26,28,35,36,37,38,62,69,70,72,73,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,118,122,124,129,130,140,143,167,],[55,-82,-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,55,-82,-58,-61,55,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,None,55,-62,-63,55,55,55,-71,55,-33,-79,-77,55,55,55,-78,]),'LOR':([4,14,20,21,22,23,24,25,26,28,35,36,37,38,62,69,70,72,73,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,118,122,124,129,130,140,143,167,],[56,-82,-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,56,-82,-58,-61,56,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-59,None,-62,-63,56,56,56,-71,56,-33,-79,-77,56,56,56,-78,]),'BAND':([4,14,20,21,22,23,24,25,26,28,35,36,37,38,62,69,70,72,73,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,118,122,124,129,130,140,143,167,],[57,-82,-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,57,-82,-58,-61,57,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,57,57,None,57,57,57,57,-71,57,-33,-79,-77,57,57,57,-78,]),'BOR':([4,14,20,21,22,23,24,25,26,28,35,36,37,38,62,69,70,72,73,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,110,118,122,124,129,130,140,143,167,],[58,-82,-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,58,-82,-58,-61,58,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,58,58,-62,None,58,58,58,-71,58,-33,-79,-77,58,58,58,-78,]),'LBRACKET':([14,27,39,70,71,157,],[64,74,-81,64,74,163,]),'EQUALS':([14,62,65,75,109,129,],[66,-82,106,112,128,144,]),'DOT':([14,],[67,]),'COLON':([14,],[68,]),'RPAREN':([20,21,22,23,24,25,26,28,35,36,37,38,62,63,69,70,72,73,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,104,110,118,122,124,129,131,140,146,147,160,165,167,],[-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,-34,110,-82,-58,-61,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-59,-60,-62,-63,122,-35,-71,136,-33,-79,-77,-29,-36,158,-30,-32,-31,-78,]),'COMMA':([20,21,22,23,24,25,26,28,35,36,37,38,62,63,70,72,73,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,103,104,108,110,122,124,125,127,129,131,132,133,135,138,140,141,146,147,151,160,161,164,165,167,],[-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,-34,-82,-58,-61,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-59,-60,-62,-63,123,-35,-34,-71,-33,-79,-34,123,-77,-29,150,-25,-28,-3,-36,123,159,-30,-27,-32,-26,-4,-31,-78,]),'RBRACKET':([20,21,22,23,24,25,26,28,35,36,37,38,62,70,72,73,74,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,105,110,122,124,129,166,167,],[-64,-65,-66,-67,-68,-69,-70,-72,-73,-74,-75,-76,-82,-82,-58,-61,111,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-56,-57,-59,-60,-62,-63,124,-71,-33,-79,-77,167,-78,]),'LBRACE':([33,62,66,79,80,84,106,136,139,158,],[83,-82,108,116,83,83,125,-23,83,83,]),'ELSE':([121,138,],[139,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'scope':([0,83,],[2,120,]),'statement':([0,2,83,120,],[3,40,3,40,]),'expr':([0,2,17,18,19,29,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,63,64,66,81,83,108,112,120,123,125,128,],[4,4,69,72,73,76,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,104,105,107,118,4,104,130,4,140,104,143,]),'var_declaration':([0,2,83,120,],[5,5,5,5,]),'return':([0,2,83,120,],[6,6,6,6,]),'assign':([0,2,83,120,],[7,7,7,7,]),'func_declaration':([0,2,83,116,120,150,],[8,8,8,135,8,135,]),'struct_declaration':([0,2,83,120,],[9,9,9,9,]),'while':([0,2,83,120,],[10,10,10,10,]),'goto_mark':([0,2,83,120,],[15,15,15,15,]),'if-else':([0,2,83,120,],[16,16,16,16,]),'id':([0,2,14,17,18,19,27,29,31,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,63,64,66,78,81,83,108,111,112,120,123,125,128,],[20,20,65,20,20,20,75,20,79,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,115,20,20,20,129,20,20,20,20,20,]),'int':([0,2,17,18,19,29,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,63,64,66,81,83,108,112,120,123,125,128,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'double':([0,2,17,18,19,29,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,63,64,66,81,83,108,112,120,123,125,128,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'bool':([0,2,17,18,19,29,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,63,64,66,81,83,108,112,120,123,125,128,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'str':([0,2,17,18,19,29,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,63,64,66,81,83,108,112,120,123,125,128,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'void':([0,2,17,18,19,29,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,63,64,66,81,83,108,112,120,123,125,128,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'datatype':([0,2,17,18,19,29,30,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,63,64,66,81,83,108,112,120,123,125,128,144,],[27,27,71,71,71,71,78,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,27,71,71,27,71,71,71,157,]),'conditional':([32,34,119,],[80,84,137,]),'basic_block':([33,80,84,139,158,],[82,117,121,153,164,]),'args':([63,108,125,],[103,127,141,]),'struct_params':([116,],[132,]),'struct_param':([116,150,],[133,161,]),'params':([131,],[146,]),'param':([131,159,],[147,165,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> <empty>','program',0,'p_program','doh_parser.py',34),
  ('program -> scope','program',1,'p_program','doh_parser.py',35),
  ('basic_block -> LBRACE scope RBRACE','basic_block',3,'p_body_block','doh_parser.py',44),
  ('func_declaration -> FUNCTION datatype id LPAREN params RPAREN basic_block','func_declaration',7,'p_func_declaration','doh_parser.py',50),
  ('scope -> scope statement','scope',2,'p_scope','doh_parser.py',55),
  ('scope -> statement','scope',1,'p_scope','doh_parser.py',56),
  ('statement -> expr SEMI','statement',2,'p_stmt','doh_parser.py',65),
  ('statement -> var_declaration','statement',1,'p_stmt','doh_parser.py',66),
  ('statement -> return','statement',1,'p_stmt','doh_parser.py',67),
  ('statement -> assign','statement',1,'p_stmt','doh_parser.py',68),
  ('statement -> func_declaration','statement',1,'p_stmt','doh_parser.py',69),
  ('statement -> struct_declaration','statement',1,'p_stmt','doh_parser.py',70),
  ('statement -> while','statement',1,'p_stmt','doh_parser.py',71),
  ('statement -> BREAK SEMI','statement',2,'p_stmt','doh_parser.py',72),
  ('statement -> CONTINUE SEMI','statement',2,'p_stmt','doh_parser.py',73),
  ('statement -> GOTO ID SEMI','statement',3,'p_stmt','doh_parser.py',74),
  ('statement -> goto_mark','statement',1,'p_stmt','doh_parser.py',75),
  ('statement -> if-else','statement',1,'p_stmt','doh_parser.py',76),
  ('while -> WHILE conditional basic_block','while',3,'p_loops','doh_parser.py',90),
  ('while -> DO basic_block WHILE conditional SEMI','while',5,'p_loops','doh_parser.py',91),
  ('if-else -> IF conditional basic_block','if-else',3,'p_if_else','doh_parser.py',101),
  ('if-else -> IF conditional basic_block ELSE basic_block','if-else',5,'p_if_else','doh_parser.py',102),
  ('conditional -> LPAREN expr RPAREN','conditional',3,'p_conditional','doh_parser.py',111),
  ('struct_declaration -> STRUCTURE id LBRACE struct_params RBRACE','struct_declaration',5,'p_struct_declaration','doh_parser.py',117),
  ('struct_params -> struct_param','struct_params',1,'p_struct_params','doh_parser.py',124),
  ('struct_params -> struct_params COMMA struct_param','struct_params',3,'p_struct_params','doh_parser.py',125),
  ('struct_param -> DATATYPE ID','struct_param',2,'p_struct_param','doh_parser.py',135),
  ('struct_param -> func_declaration','struct_param',1,'p_struct_param','doh_parser.py',136),
  ('params -> <empty>','params',0,'p_params','doh_parser.py',145),
  ('params -> param','params',1,'p_params','doh_parser.py',146),
  ('params -> params COMMA param','params',3,'p_params','doh_parser.py',147),
  ('param -> DATATYPE ID','param',2,'p_param_declaration','doh_parser.py',157),
  ('expr -> ID LPAREN args RPAREN','expr',4,'p_func_call','doh_parser.py',162),
  ('args -> <empty>','args',0,'p_arguments','doh_parser.py',167),
  ('args -> expr','args',1,'p_arguments','doh_parser.py',168),
  ('args -> args COMMA expr','args',3,'p_arguments','doh_parser.py',169),
  ('var_declaration -> datatype id EQUALS expr SEMI','var_declaration',5,'p_var_declaration','doh_parser.py',181),
  ('var_declaration -> datatype id SEMI','var_declaration',3,'p_var_declaration','doh_parser.py',182),
  ('var_declaration -> ID id EQUALS LBRACE args RBRACE SEMI','var_declaration',7,'p_var_declaration','doh_parser.py',183),
  ('assign -> ID EQUALS expr SEMI','assign',4,'p_assign','doh_parser.py',195),
  ('assign -> ID EQUALS LBRACE args RBRACE SEMI','assign',6,'p_assign','doh_parser.py',196),
  ('assign -> ID DOT ID EQUALS expr SEMI','assign',6,'p_assign','doh_parser.py',197),
  ('return -> RETURN expr SEMI','return',3,'p_return','doh_parser.py',208),
  ('return -> RETURN SEMI','return',2,'p_return','doh_parser.py',209),
  ('expr -> expr PLUS expr','expr',3,'p_math_expressions','doh_parser.py',218),
  ('expr -> expr MINUS expr','expr',3,'p_math_expressions','doh_parser.py',219),
  ('expr -> expr MUL expr','expr',3,'p_math_expressions','doh_parser.py',220),
  ('expr -> expr DIVIDE expr','expr',3,'p_math_expressions','doh_parser.py',221),
  ('expr -> expr INTDIVIDE expr','expr',3,'p_math_expressions','doh_parser.py',222),
  ('expr -> expr MODULO expr','expr',3,'p_math_expressions','doh_parser.py',223),
  ('expr -> expr POW expr','expr',3,'p_math_expressions','doh_parser.py',224),
  ('expr -> expr LE expr','expr',3,'p_conditionals','doh_parser.py',245),
  ('expr -> expr GE expr','expr',3,'p_conditionals','doh_parser.py',246),
  ('expr -> expr LT expr','expr',3,'p_conditionals','doh_parser.py',247),
  ('expr -> expr GT expr','expr',3,'p_conditionals','doh_parser.py',248),
  ('expr -> expr EQ expr','expr',3,'p_conditionals','doh_parser.py',249),
  ('expr -> expr NE expr','expr',3,'p_conditionals','doh_parser.py',250),
  ('expr -> MINUS expr','expr',2,'p_logical_operation','doh_parser.py',266),
  ('expr -> expr LAND expr','expr',3,'p_logical_operation','doh_parser.py',267),
  ('expr -> expr LOR expr','expr',3,'p_logical_operation','doh_parser.py',268),
  ('expr -> LNOT expr','expr',2,'p_logical_operation','doh_parser.py',269),
  ('expr -> expr BAND expr','expr',3,'p_bitwise_operation','doh_parser.py',282),
  ('expr -> expr BOR expr','expr',3,'p_bitwise_operation','doh_parser.py',283),
  ('expr -> id','expr',1,'p_literals','doh_parser.py',292),
  ('expr -> int','expr',1,'p_literals','doh_parser.py',293),
  ('expr -> double','expr',1,'p_literals','doh_parser.py',294),
  ('expr -> bool','expr',1,'p_literals','doh_parser.py',295),
  ('expr -> str','expr',1,'p_literals','doh_parser.py',296),
  ('expr -> void','expr',1,'p_literals','doh_parser.py',297),
  ('expr -> NULL','expr',1,'p_literals','doh_parser.py',298),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_literals','doh_parser.py',299),
  ('int -> INTEGER','int',1,'p_const_int','doh_parser.py',307),
  ('double -> DOUBLE','double',1,'p_const_double','doh_parser.py',312),
  ('bool -> BOOL','bool',1,'p_const_bool','doh_parser.py',317),
  ('str -> STRING','str',1,'p_const_string','doh_parser.py',322),
  ('void -> VOID','void',1,'p_void','doh_parser.py',327),
  ('expr -> datatype LBRACKET RBRACKET id','expr',4,'p_array_init','doh_parser.py',333),
  ('expr -> datatype LBRACKET RBRACKET id EQUALS datatype LBRACKET INTEGER RBRACKET','expr',9,'p_array_init','doh_parser.py',334),
  ('expr -> ID LBRACKET expr RBRACKET','expr',4,'p_index','doh_parser.py',343),
  ('goto_mark -> ID COLON','goto_mark',2,'p_goto_mark','doh_parser.py',348),
  ('datatype -> DATATYPE','datatype',1,'p_datatype','doh_parser.py',353),
  ('id -> ID','id',1,'p_id','doh_parser.py',358),
]

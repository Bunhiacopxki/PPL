// Nguyễn Thái Tân - 2112256

grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: nullable_newline_list decl_list EOF;
decl_list: decl decl_list | decl;
decl: var_decl | func_decl;

var_decl: var_decl_part newline_list;
var_decl_part: optional_vardecl | must_vardecl | arr_decl;
optional_vardecl: (scalar_type | DYNAMIC) IDENTIFIER optional_initialize;
must_vardecl: VAR IDENTIFIER initialize;
arr_decl: scalar_type IDENTIFIER arr_size_list optional_initialize;
arr_size_list: LS arr_size_prime RS;
arr_size_prime: NUMBERLIT | arr_size_prime COMMA NUMBERLIT;
scalar_type: NUMBER | BOOL | STRING;
optional_initialize: initialize | ;
initialize: ASSIGN expr;

func_decl: FUNC IDENTIFIER param_decl endfunc;
param_decl: LP param_list RP;
param_list: param_prime |;
param_prime: param COMMA param_prime | param;
param: scalar_type param_name;
param_name: IDENTIFIER | IDENTIFIER arr_size_list;
endfunc: nullable_newline_list blockstmt | nullable_newline_list returnstmt newline_list | newline_list;


assignstmt: lhs ASSIGN expr;
lhs: IDENTIFIER | (IDENTIFIER LS index_operators RS);

// Expression
literal: NUMBERLIT | BOOLLIT | STRINGLIT;

expr: expr1;
expr1: expr2 CONCAT expr2 | expr2;
expr2: expr3 RELOP expr3 | expr3;
expr3: expr3 (AND | OR) expr4 | expr4;
expr4: expr4 (ADD | SUB) expr5 | expr5;
expr5: expr5 (MUL | DIV | MOD) expr6 | expr6;
expr6: NOT expr6 | expr7;
expr7: SUB expr7 | expr8;
expr8: LS (index_operators | ) RS | index_operation | expr9;
expr9: LP expr RP | literal | IDENTIFIER | callstmt;

index_operation: expr9 LS index_operators RS;
index_operators: expr | expr COMMA index_operators;

// Statement
ifstmt: IF cond_block optional_elif_list | IF cond_block optional_elif_list optional_else;
cond_block: LP expr RP nullable_newline_list stmt;
optional_elif_list: optional_elif | ;
optional_elif: ELIF cond_block optional_elif | ELIF cond_block;
optional_else: ELSE nullable_newline_list stmt;

forstmt: FOR IDENTIFIER UNTIL expr BY expr nullable_newline_list stmt;

breakstmt: BREAK;
continuestmt: CONTINUE;
returnstmt: RETURN | RETURN expr;

callstmt: IDENTIFIER paramcall_part;
paramcall_part: LP paramcall_list RP;
paramcall_list: paramcall_prime |;
paramcall_prime: paramcall COMMA paramcall_prime | paramcall;
paramcall: expr | IDENTIFIER | IDENTIFIER paramcall;

blockstmt: BEGIN newline_list stmt_list END newline_list;

stmt_list: stmt_prime |;
stmt_prime: stmt stmt_prime | stmt;
stmt: assignstmt newline_list
     | ifstmt 
     | forstmt
     | breakstmt newline_list
     | continuestmt newline_list
     | callstmt newline_list
     | blockstmt
     | returnstmt newline_list
     | var_decl
    ;

nullable_newline_list: newline_list | ;
newline_list: NEWLINE newline_list | NEWLINE;

fragment LETTER: [a-zA-Z_];
fragment DIGIT: [0-9];
fragment CHAR: ~[\r\n"\\] | ESCSEQ | [']["];
fragment ESCSEQ: '\\' [btnfr'\\];

// Literal
fragment INTPART: DIGIT+;
fragment DECPART: '.' DIGIT*;
fragment EXPART: ('e' | 'E') ('+' | '-')? DIGIT+;
NUMBERLIT: INTPART DECPART? EXPART?;
BOOLLIT: TRUE | FALSE;
STRINGLIT: '"' CHAR* '"' {self.text = self.text[1:-1]};

// KEYWORD
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT: 'not';
AND: 'and';
OR: 'or';

ADD: '+';
SUB: '-';
MUL: '*'; 
DIV: '/'; 
MOD: '%'; 
ASSIGN: '<-';

LP: '(';
RP: ')';
LS: '[';
RS: ']';
COMMA: ',';
RELOP: '=='
      | '!='
      | '<'
      | '>'
      | '<='
      | '>='
      | '='
     ;
CONCAT: '...';
NEWLINE: '\n';

CMT: '##' ~[\n]* -> skip;
WS: [ \r\t\b\f]+ -> skip; 

IDENTIFIER: (LETTER) (LETTER | DIGIT)*;

ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: '"' CHAR* ('\r\n' | '\n' | EOF) {
	if (len(self.text) >= 2 and self.text[-2] == '\r' and self.text[-1] == '\n'):
          raise UncloseString(self.text[1:-2])
	elif (self.text[-1] == '\n'):
		raise UncloseString(self.text[1:-1])
	else:
          raise UncloseString(self.text[1:])
};
fragment ILLEGAL_ESCSEQ: '\\' ~[bfrnt'\\];
ILLEGAL_ESCAPE: '"' CHAR* ILLEGAL_ESCSEQ {raise IllegalEscape(self.text[1:])};

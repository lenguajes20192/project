grammar Python3;

inicio  : 'hola' ID (',' ID)* ;
ID : 	[a-zA-Z]+ ;
ESP : [ \t\r\n]+ -> skip ;

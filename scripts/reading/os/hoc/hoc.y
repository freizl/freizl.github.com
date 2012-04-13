%{
#define YYSTYPE double /* data type of yacc stack */
#include <stdio.h>
#include <ctype.h>
  %}
%token NUMBER
%left '*' '/'
%left '+' '-'
%%
list: /* nothing */
| list '\n'
| list expr '\n' { printf("\t= %.8g\n", $2); }
;
expr:  NUMBER { $$ = $1; }
| expr '+' expr { $$ = $1 + $3; }
| expr '-' expr { $$ = $1 - $3; }
| expr '*' expr { $$ = $1 * $3; }
| expr '/' expr { $$ = $1 / $3; }
| '(' expr ')' { $$ = $2; }
;
%%
char *progname; /* for erro message */
int lineno = 1;

warning(s,t)
char *s, *t;
{
  fprintf(stderr, "%s: %s", progname, s);
  if (t)
    fprintf(stderr, " %s", t);
  fprintf(stderr, " near line %d\n", lineno);
}

yyerror(s)
char *s;
{
  warning(s, (char *) 0);
}

yylex()
{
  int c;
  while ((c=getchar()) == ' ' || c == '\t');
  if (c == EOF)
    return 0;
  if (c == '.' || isdigit(c)) {
    ungetc(c, stdin);
    scanf("%lf", &yylval);
    /*    printf("%lf", c); */
    return NUMBER;
  }
  /*  printf("%d,++,", c); */
  if (c == '\n')
    lineno++;
  return c;
}

main(argc, argv) 
char *argv[];
{
  progname = argv[0];
  yyparse();
}


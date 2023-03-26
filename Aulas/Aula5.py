import ply.lex as lex

tokens=(
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "PAROPEN",
    "PARCLOSE"
)

t_PLUS=r"\+"
t_DIVIDE=r"\/"
t_TIMES=r"\*"
t_PAROPEN=r"\("
t_PARCLOSE=r"\)"
t_ignore=" \t\n"



#a primeira linha é a documentação da função
def t_NUMBER(t):
    r"-?\d+"
    t.value=int(t.value)
    return t

def t_MINUS(t):
    r"-"
    return t
def t_error(t):
    print(f"Character Illegal {t.value}")
    t.lexer.skip(1)


lexer = lex.lex()

data="""
    3 + 4 * 10
      + -20 *2
"""

#lexer.input(data)

while data := input() :
   lexer.input(data)
   while tok := lexer.token() :
        print(tok)
#exemplo da aula do ply

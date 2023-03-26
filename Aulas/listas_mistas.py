import ply.lex as lex

tokens=(
    "PARINIT",
    "PARCLOSE",
    "NUMERO",
    "FRASE",
    "BOOLEAN",
    "PI",
    "PE",
    "PF",
    "VIRGULA"
)

t_PARINIT="\["
t_PARCLOSE="\]"
t_NUMERO="-?\d+.?\d+"
t_FRASE="\w+"
t_PI="\?"
t_PE="\!"
t_PF="\."
t_ignore=" \t\n,"

def t_BOOLEAN(t):
    r"(False|True)"
    if t.value=="True":
        t.value = True
    else :t.value = False
    return t

def t_error(t):
    print(f"Character Illegal {t.value}")
    t.lexer.skip(1)

lexer = lex.lex()

while data := input() :
   lexer.input(data)
   while tok := lexer.token():
        print(tok)
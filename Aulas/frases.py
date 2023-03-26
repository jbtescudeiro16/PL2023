import ply.lex as lex

tokens=(
    "FRASE",
    "PONTO",
    "VIRGULA",
    "EXCLAMA",
    "INTERROGA"
)

t_FRASE=r"\w+"
t_PONTO=r"\."
t_VIRGULA=r"\,"
t_EXCLAMA=r"\!"
t_INTERROGA=r"\?"
t_ignore=" \t\n"
def t_error(t):
    print(f"Character Illegal {t.value}")
    t.lexer.skip(1)

lexer = lex.lex()

data="""
    O meu nome é joao.
    """
#lexer.input(data)

while data := input() :
   lexer.input(data)
   while tok := lexer.token():
        print(tok)

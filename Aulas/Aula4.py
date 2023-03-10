import re


def iso_86012():
    res = []
    texto = """A 03/01/2022, Pedro viajou para a praia com a sua família.
    Eles ficaram hospedados num hotel e aproveitaram o sol e o mar durante toda a semana.
    Mais tarde, no dia 12/01/2022, Pedro voltou para casa e começou a trabalhar num novo projeto.
    Ele passou muitas horas no escritório, mas finalmente terminou o projeto a 15/01/2022."""

    print( re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\3-\2-\1",texto))




def iso_8601():
    res = []
    texto = """A 03/01/2022, Pedro viajou para a praia com a sua família.
    Eles ficaram hospedados num hotel e aproveitaram o sol e o mar durante toda a semana.
    Mais tarde, no dia 12/01/2022, Pedro voltou para casa e começou a trabalhar num novo projeto.
    Ele passou muitas horas no escritório, mas finalmente terminou o projeto a 15/01/2022."""

    aux = re.findall(r"\b[0-9]{2}/[0-9]{2}/[0-9]{4}\b",texto)



    for i in aux :
        partido= re.split(r"/",i)
        res.append((partido[2]+"/"+partido[1]+"/"+partido[0]))
    return res


def validatefiles():
    valid=[]
    file_names = [
        "document.txt",  # válido
        "file name.docx",  # inválido
        "image_001.jpg",  # válido
        "script.sh.txt",  # válido
        "test_file.txt",  # válido
        "file_name.",  # inválido
        "my_resume.docx",  # válido
        ".hidden-file.txt",  # válido
        "important-file.text file",  # inválido
        "file%name.jpg"  # inválido
    ]
    for i in file_names:

         if (re.match(r"^(\w|\.|-)+(\.)(txt|jpg|png|docx)$",i) !=None):
            valid.append(i)
    return  valid


#inacabado
def nameConverter():
    texto = """Este texto foi feito por Sofia Guilherme Rodrigues dos Santos, com 
    base no texto original de Pedro Rafael Paiva Moura, com a ajuda
    dos professores Pedro Rangel Henriques e José João Antunes Guimarães Dias De Almeida.
    Apesar de partilharem o mesmo apelido, a Sofia não é da mesma família do famoso
    autor José Rodrigues dos Santos."""

    return re.findall(r"\b([A-Z][\w]+)(\s[A-Z][\w]+)(\s[A-Z][\w]+) ",texto)


def codigos_postais():
    listavalido=[]
    lista = [
        "4700-000",  # válido
        "9876543",  # inválido
        "1234-567",  # válido
        "8x41-5a3",  # inválido
        "84234-12",  # inválido
        "4583--321",  # inválido
        "9481-025"  # válido
    ]
    for i in lista :
       if  re.match(r"^[0-9]{4}-[0-9]{3}",i)!=None :
           aux =re.split(r"-",i)
           listavalido.append((aux[0],aux[1]))

    return listavalido

def expand_abrev():
    abreviaturas = {
        "UM": "Universidade do Minho",
        "LEI": "Licenciatura em Engenharia Informática",
        "UC": "Unidade Curricular",
        "PL": "Processamento de Linguagens"
    }
    texto = "A /abrev{UC} de /abrev{PL} é muito fixe! É uma /abrev{UC} que acrescenta muito ao curso de /abrev{LEI} da /abrev{UM}."
    for i in abreviaturas:
        expr=r"/abrev{"+i+"}"
        aux =re.sub(expr,abreviaturas[i],texto)
        texto=aux
    return texto

#nao esta bem
def matricula_valida():
    matricua_val=[]
    matriculas = [
        "AA-AA-AA",  # inválida
        "LR-RB-32",  # válida
        "1234LX",  # inválida
        "PL 22 23",  # válida
        "ZZ-99-ZZ",  # válida
        "54-tb-34",  # inválida
        "12 34 56",  # inválida
        "42-HA BQ"  # válida, mas inválida com o requisito extra
    ]
    for i in matriculas:
        padrao1=r"^([A-Z]{2}[ -]{1}[0-9]{2}[ -]{1}[A-Z]{2})$"

if __name__ == '__main__':
     #print(iso_8601())
     #print(iso_86012())
     #print(validatefiles())
     #print(nameConverter())
     #print(codigos_postais())
     #print(expand_abrev())
     matricula_valida()
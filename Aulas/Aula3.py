import re
def alineadois():
    line1 = "hello world"
    line2 = "goodbye world"
    line3 = "hi, hello there"
    print(re.match(r"hello", line1))


#def alineadois():
#    for line in
#        print(re.search(r"hello"))

def alineatres():
    line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
    print(re.findall(r"hello",line))

def alineaquatro():
    line = "Hello there! Uh, hi, hello, it's me... Heyyy, hello? HELLO!"
    print(re.sub(r"(?i:hello)","Boas",line))

def alineacinco():
    line = "bananas, laranjas, maçãs, uvas, melancias, cerejas, kiwis, etc."
    print(re.split(r",",line))

def palavra_magica(frase):
    return re.search(r"(por favor[!?.]+)$",frase)

def narcissismo(frase):
    return len(re.findall(r"(?i:eu)",frase))

def troca_de_curso(linha, novo_curso):
  return re.sub(r"(?i:lei)",novo_curso,linha)

def soma_string(linha):
    k=re.split(r",",linha)
    soma = 0
    aux=[]
    for i in k:
        aux+= re.findall(r"[-]*[0-9]+",i)
    for num in aux:
        soma+=(int(num))
    return soma

#usamos o b para garantir que o match são palavras
def pronomes(linha):
    return re.findall(r"(?i:\b(eu|tu|nós|vós|eles|ela|ele)\b)",linha)

def variavel_valida(linha):
    if (re.match(r"(?i:^[a-z]+[0-9]*[_]*)",linha)): return True
    else : return False

def inteiros(linha):
    return re.findall(r"[-]*[0-9]+",linha)

def underscores(linha):
    return re.sub(r"[ ]+","_",linha)

def codigospostais(lista):
    nova=[]
    for i in lista:
        res=re.split(r"[-]",i)
        nova.append((res[0],res[1]))
    return nova




if __name__ == '__main__':
    #alineaum()
    #alineaquatro()
    #alineacinco()
    #print(palavra_magica("por favor?"))
    #print(palavra_magica("Posso ir à casa de banho, por favor!"))
    #print(palavra_magica("Preciso de um favor."))
    #print(narcissismo("Eu não sei se eu quero continuar a ser eu. Por outro lado, eu ser eu é uma parte importante de quem EU sou."))
    #print(troca_de_curso("LEI é o melhor curso! Adoro LEI! Gostar de LEI devia ser uma lei.","MIEGI"))
    #print(soma_string("4,-6,2,3,8,-3,0,2,-5,1"))
    #print(pronomes("eu comi um gelado do mac mas elEs também queriam"))
    #print(variavel_valida("_asdsdas_"))
    #print(inteiros("1234-123412 32"))
    #print(underscores("asaaac assda     a a "))
    print(codigospostais(["5430-504","54023-504","5340-30"]))

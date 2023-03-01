import json
import re
from collections import defaultdict

dicionario=dict()

def aux():
    #dictinit()
    a=open("files/processos.txt")
    for k in a:

        x=re.split(r"::",k)
        year = re.findall(r"^[0-9]{4}",x[1])[0]

        if year in dicionario :
            dicionario[year].append((x[0],x[1],x[2],x[3],x[4],x[5]))
        else :
            dicionario[year] =[]
            dicionario[year].append((x[0],x[1],x[2],x[3],x[4],x[5]))
"""
    for i in dicionario:
        print("chave"+i)
        for pos in dicionario[i]:
            print(pos)
"""
#tenho um dicionario em que as chaves sao os anos do processo


def getregsbyyear(ano):

    if ano  in dicionario : return  len(dicionario[ano])
    else : return 0




def namepopular(anobaixo,anocima):
    contanomes=dict()
    contaapelidos=dict()
    for key in dicionario:
        if (int(key) >=anobaixo and int(key) <=anocima ) :
            for posicao in dicionario[key]:

                cont=2
                while cont<5:
                    if posicao[cont]!="":
                         nome=re.findall(r"(?i:^[a-z]+)",posicao[cont])[0]
                         if nome in contanomes :
                            contanomes[nome]+=1
                         else:
                            contanomes[nome]=1

                         a=re.findall(r"(?i:[a-z]+$)", posicao[cont])


                         if a !=[]:
                             apelido =a[0]
                             if apelido in contaapelidos:
                                 contaapelidos[apelido]+=1
                             else :
                                 contaapelidos[apelido]=1
                    cont+=1;
    """
    max = 0   
    for a in contanomes:

        if contanomes[a]>max:
            max=contanomes[a]
            nameaux=a
        print("Nome "+a + " , Frequencia "+str(contanomes[a]))
    print("o max "+str(max) + " Nome "+ nameaux)
    """
    sorted_items = sorted(contanomes.items(), key=lambda x: x[1], reverse=True)
    top_items = sorted_items[:5]

    sit = sorted(contaapelidos.items(), key=lambda x: x[1], reverse=True)
    sunames = sit[:5]


    return (top_items,sunames)

def nomesmaispopulares():
    min =1600
    while(min<2000):
        print("########################################################")
        print(f"Os nomes mais populares no seculo {(min+99 - 1) // 100 + 1} ")
        a = namepopular(min,min+99)

        for i in a[0]:
            print(f"Nome : {i[0]} , Frequência :{i[1]}")

        print("------------------------------------------------")
        print(f"Os Apelidos mais populares no seculo {(min + 99 - 1) // 100 + 1} ")

        for i in a[1]:
            print(f"Apelido : {i[0]} , Frequência :{i[1]}")



        min+=100
        print("########################################################")

#acabar os irmaos
def kinship():
    relacoes=dict()
    for i in dicionario:
        for val in dicionario[i]:
            print(val[5])
            #a= re.findall(r"(?i:[a-z]+,[pai]{1})",val[5])
            a = re.findall(r"(?i:[a-z]+,(irmao))",val[5])
            if a!=[] :
                print(a)

def writeJson():
    auxiliar=dict()
    k=open("files/processos.txt")
    f =open("files/novo,json","w")
    num = 1

    for line in k:
            if num > 20:
                break

            x = re.split(r"::", line)
            year = re.findall(r"^[0-9]{4}", x[1])[0]

            if year in auxiliar:
                auxiliar[year].append((x[0], x[1], x[2], x[3], x[4], x[5]))
            else:
                auxiliar[year] = []
                auxiliar[year].append((x[0], x[1], x[2], x[3], x[4], x[5]))
            num = num + 1
    json.dump(auxiliar,f)
    k.close()
    f.close()



if __name__ == '__main__':
    aux()
    print("-------------------TPC3-A96075--------------------------------")
    print("| 1-> Obter a frequência de processos por ano                |")
    print("| 2-> Obter os nomes  mais frequentes por século             |")
    print("| 3-> Obter a frequência de Graus de Parentesco              |")
    print("| 4-> Escrever para um ficheiro JSON                         |")
    print("--------------------------------------------------------------")
    opt=input()
    if opt=="1" :
        print("Insira o ano que pretende obter:")
        year =input()
        print( f"O total de registos no ano de {year} foi :{getregsbyyear(year)}")
    if opt=="2" :
         nomesmaispopulares()
    if opt=="3" :
         kinship()
    if opt=="4" :
         writeJson()




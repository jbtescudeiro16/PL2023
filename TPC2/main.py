


def parsercommandline():
    soma = 0;
    k=input()
    while k!='':
        text = k
        i = 0
        while i < len(text):
            if text[i].isdigit():
                seq = text[i]
                j = i + 1
                while j < len(text) and text[j].isdigit():
                    seq += text[j]
                    j += 1
                soma += int(seq)
                i = j
            else:
                if text[i] =="=":
                    print("A soma está em: "+str(soma))
                i += 1
        k=input()

    print( soma)
def parser(filepath):
    soma=0;
    with open(filepath, 'r') as file:
        text = file.read()
        i = 0
        while i < len(text):
            if text[i].isdigit():
                seq = text[i]
                j = i + 1
                while j < len(text) and text[j].isdigit():
                    seq += text[j]
                    j += 1
                soma += int(seq)
                i = j
            else:
                if text[i] =="=":
                    print("A soma está em: "+str(soma))
                i += 1

        print( "A soma dos digitos no ficheiro é:"+str(soma))
if __name__ == '__main__':
    print("------------PL2023-TPC2-A96075------------")
    print("|Insira de onde pretende obter o Input : |")
    print("|1-> Ficheiro                            |")
    print("|2->Linha de Comandos                    |")
    print("------------------------------------------")
    opt=input()
    if opt=='1':
        parser("files/auxiliar.txt")
    elif (opt=='2'):
        parsercommandline()


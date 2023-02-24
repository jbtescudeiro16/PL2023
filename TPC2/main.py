


def parsercommandline():
    ligado=1
    soma = 0;
    k=input()
    while k!='':
        text = k
        i = 0
        while i < len(text):
            if text[i].isdigit() and ligado==1:
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
                elif (text[i] == "O" or text[i] == "o"):
                    if i + 1 < len(text):
                        j = i + 1
                        if (text[j] == "f" or text[j] == "F"):
                            if (i + 2 < len(text)):
                                k = i + 2
                                if (text[k] == "f" or text[k] == "F"):
                                    ligado=0
                        elif (text[j] == "n" or text[j] == "N"):
                                    ligado=1

                i += 1
        k=input()

    print("O resultado final é: " +str(soma))
def parser(filepath):
    ligado=1
    soma=0
    with open(filepath, 'r') as file:
        text = file.read()
        i = 0
        while i < len(text):
            if text[i].isdigit() and ligado==1:
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
                elif (text[i] == "O" or text[i] == "o"):
                    if i + 1 < len(text):
                        j = i + 1
                        if (text[j] == "f" or text[j] == "F"):
                            if (i + 2 < len(text)):
                                k = i + 2
                                if (text[k] == "f" or text[k] == "F"):
                                    ligado=0
                        elif (text[j] == "n" or text[j] == "N"):
                                    ligado=1
                i += 1

        print("O resultado final é: " +str(soma))



if __name__ == '__main__':
    print("------------PL2023-TPC2-A96075------------")
    print("|Insira de onde pretende obter o Input : |")
    print("|1-> Ficheiro                            |")
    print("|2-> Linha de Comandos                    |")
    print("------------------------------------------")
    opt=input()
    if opt=='1':
        parser("files/auxiliar.txt")
    elif (opt=='2'):
        parsercommandline()


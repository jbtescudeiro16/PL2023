from prettytable import PrettyTable









mydictionar = dict()

def getage(val):
    return int(val[0])

def getvol(val):
    return int(val[2])


def calculadistrcolesterol():
    zeronoveP=0
    dezdezanoveP=0
    vintevintenoveP=0
    trintatrintanoveP=0
    quarentaquarentanoveP=0
    cinquentacinquentanoveP=0
    sessentasessentanoveP=0
    setentasetentanoveP=0
    oitentaoitentanoveP=0
    noventanoventanoveP=0
    cemcemnoveP=0
    cemdezcemdezanoveP=0
    cemvintecemvintenoveP=0
    cemtrintacemtrintanoveP=0
    cemquarentacemquarentanoveP=0
    intermedioP=0
    seiscentosseiscentosnoveP=0

    zeronoveI = 0
    dezdezanoveI = 0
    vintevintenoveI = 0
    trintatrintanoveI = 0
    quarentaquarentanoveI = 0
    cinquentacinquentanoveI = 0
    sessentasessentanoveI = 0
    setentasetentanoveI = 0
    oitentaoitentanoveI = 0
    noventanoventanoveI = 0
    cemcemnoveI = 0
    cemdezcemdezanoveI = 0
    cemvintecemvintenoveI = 0
    cemtrintacemtrintanoveI = 0
    cemquarentacemquarentanoveI = 0
    intermedioI= 0
    seiscentosseiscentosnoveI = 0

    for i in mydictionar:
        for k in mydictionar[i]:
            if (i == "MP" or i == "FP"):
                if (getvol(k) >= 0 and getvol(k) <= 9):
                    zeronoveP += 1
                elif (getvol(k) >= 10 and getvol(k) <= 19):
                    dezdezanoveP += 1
                elif (getvol(k) >= 20 and getvol(k) <= 29):
                    vintevintenoveP += 1
                elif (getvol(k) >= 30 and getvol(k) <= 39):
                    trintatrintanoveP += 1
                elif (getvol(k) >= 40 and getvol(k) <= 49):
                    quarentaquarentanoveP += 1
                elif (getvol(k) >= 50 and getvol(k) <= 59):
                    cinquentacinquentanoveP += 1
                elif (getvol(k) >= 60 and getvol(k) <= 69):
                    sessentasessentanoveP += 1
                if (getvol(k) >= 70 and getvol(k) <= 79):
                    setentasetentanoveP += 1
                elif (getvol(k) >= 80 and getvol(k) <= 89):
                    oitentaoitentanoveP += 1
                elif (getvol(k) >= 90 and getvol(k) <= 99):
                    noventanoventanoveP += 1
                elif (getvol(k) >= 100 and getvol(k) <= 109):
                    cemcemnoveP += 1
                elif (getvol(k) >= 110 and getvol(k) <= 119):
                    cemdezcemdezanoveP += 1
                elif (getvol(k) >= 120 and getvol(k) <= 129):
                    cemvintecemvintenoveP += 1
                elif (getvol(k) >= 130 and getvol(k) <= 139):
                    cemtrintacemtrintanoveP += 1
                elif (getvol(k) >= 140 and getvol(k) <= 149):
                    cemquarentacemquarentanoveP += 1
                elif (getvol(k) >= 150 and getvol(k) <= 599):
                    intermedioP += 1
                elif (getvol(k) >= 600 and getvol(k) <= 609):
                    seiscentosseiscentosnoveP += 1
            else:
                if (getvol(k) >= 0 and getvol(k) <= 9):
                    zeronoveI += 1
                elif (getvol(k) >= 10 and getvol(k) <= 19):
                    dezdezanoveI += 1
                elif (getvol(k) >= 20 and getvol(k) <= 29):
                    vintevintenoveI += 1
                elif (getvol(k) >= 30 and getvol(k) <= 39):
                    trintatrintanoveI += 1
                elif (getvol(k) >= 40 and getvol(k) <= 49):
                    quarentaquarentanoveI += 1
                elif (getvol(k) >= 50 and getvol(k) <= 59):
                    cinquentacinquentanoveI += 1
                elif (getvol(k) >= 60 and getvol(k) <= 69):
                    sessentasessentanoveI+= 1
                if (getvol(k) >= 70 and getvol(k) <= 79):
                    setentasetentanoveI += 1
                elif (getvol(k) >= 80 and getvol(k) <= 89):
                    oitentaoitentanoveI += 1
                elif (getvol(k) >= 90 and getvol(k) <= 99):
                    noventanoventanoveI += 1
                elif (getvol(k) >= 100 and getvol(k) <= 109):
                    cemcemnoveI += 1
                elif (getvol(k) >= 110 and getvol(k) <= 119):
                    cemdezcemdezanoveI += 1
                elif (getvol(k) >= 120 and getvol(k) <= 129):
                    cemvintecemvintenoveI += 1
                elif (getvol(k) >= 130 and getvol(k) <= 139):
                    cemtrintacemtrintanoveI += 1
                elif (getvol(k) >= 140 and getvol(k) <= 149):
                    cemquarentacemquarentanoveI += 1
                elif (getvol(k) >= 150 and getvol(k) <= 599):
                    intermedioI += 1
                elif (getvol(k) >= 600 and getvol(k) <= 609):
                     seiscentosseiscentosnoveI+= 1

    table = [[' ', 'Portador', 'Não Portador'],
             ["[0,9]", zeronoveP, zeronoveI],
             ["[10,19]", dezdezanoveP, dezdezanoveI],
             ["[20,29]", vintevintenoveP, vintevintenoveI],
             ["[30,39]", trintatrintanoveP, trintatrintanoveI],
             ["[40,49]", quarentaquarentanoveP, quarentaquarentanoveI],
             ["[50,59]", cinquentacinquentanoveP, cinquentacinquentanoveI],
             ["[60,69]", sessentasessentanoveP, sessentasessentanoveI],
             ["[70,79]", setentasetentanoveP, setentasetentanoveI],
             ["[80,89]", oitentaoitentanoveP, oitentaoitentanoveI],
             ["[90,99]", noventanoventanoveP, noventanoventanoveI],
             ["[100,109]", cemcemnoveP, cemcemnoveI],
             ["[110,119]", cemdezcemdezanoveP, cemdezcemdezanoveI],
             ["[120,129]", cemvintecemvintenoveP, cemvintecemvintenoveI],
             ["[130,139]", cemtrintacemtrintanoveP, cemtrintacemtrintanoveI],
             ["[140,149]", cemquarentacemquarentanoveP, cemquarentacemquarentanoveI],
             ["...", "...", "..."],
             ["[150,599]", intermedioP, intermedioI],
             ["[600,609]", seiscentosseiscentosnoveP, seiscentosseiscentosnoveI],
             ]
    tab = PrettyTable(table[0])
    tab.add_rows(table[1:])
    print(tab)







def calculaDistIdade():

 doiscincodoisnoveP =0
 treszerotresquatroP=0
 trescincotresnoveP=0
 quatrozeroquatroquatroP=0
 quatrocincoquatronoveP=0
 cincozerocincoquatroP=0
 cincocincocinconoveP=0
 seiszeroseisquatroP=0
 seiscincoseinoveP=0
 setezerosetequatroP=0
 setecincosetenoveP=0
 doiscincodoisnoveI =0
 treszerotresquatroI=0
 trescincotresnoveI=0
 quatrozeroquatroquatroI=0
 quatrocincoquatronoveI=0
 cincozerocincoquatroI=0
 cincocincocinconoveI=0
 seiszeroseisquatroI=0
 seiscincoseinoveI=0
 setezerosetequatroI=0
 setecincosetenoveI=0
 for i in mydictionar:
     for k in mydictionar[i] :
        if (i=="MP" or i== "FP"):
           if (getage(k)>=25 and getage(k)<=29):
               doiscincodoisnoveP+=1
           elif (getage(k) >= 30 and getage(k) <= 34):
               treszerotresquatroP += 1
           elif (getage(k) >= 35 and getage(k) <= 39):
               trescincotresnoveP += 1
           elif (getage(k) >= 40 and getage(k) <= 44):
               quatrozeroquatroquatroP += 1
           elif (getage(k) >= 45 and getage(k) <= 49):
               quatrocincoquatronoveP += 1
           elif (getage(k) >= 50 and getage(k) <= 54):
               cincozerocincoquatroP += 1
           elif (getage(k) >= 55 and getage(k) <= 59):
               cincocincocinconoveP += 1
           elif (getage(k) >= 60 and getage(k) <= 64):
               seiszeroseisquatroP += 1
           elif (getage(k) >= 65 and getage(k) <= 69):
               seiscincoseinoveP += 1
           elif (getage(k) >= 70 and getage(k) <= 74):
               setezerosetequatroP += 1
           elif (getage(k) >= 75 and getage(k) <= 79):
               setecincosetenoveP += 1
        else:
            if (getage(k) >= 25 and getage(k) <= 29):
                doiscincodoisnoveI += 1
            elif (getage(k) >= 30 and getage(k) <= 34):
                treszerotresquatroI += 1
            elif (getage(k) >= 35 and getage(k) <= 39):
                trescincotresnoveI += 1
            elif (getage(k) >= 40 and getage(k) <= 44):
                quatrozeroquatroquatroI += 1
            elif (getage(k) >= 45 and getage(k) <= 49):
                quatrocincoquatronoveI += 1
            elif (getage(k) >= 50 and getage(k) <= 54):
                cincozerocincoquatroI += 1
            elif (getage(k) >= 55 and getage(k) <= 59):
                cincocincocinconoveI += 1
            elif (getage(k) >= 60 and getage(k) <= 64):
                seiszeroseisquatroI += 1
            elif (getage(k) >= 65 and getage(k) <= 69):
                seiscincoseinoveI += 1
            elif (getage(k) >= 70 and getage(k) <= 74):
                setezerosetequatroI += 1
            elif (getage(k) >= 75 and getage(k) <= 79):
                setecincosetenoveI += 1

 table = [[' ', 'Portador', 'Não Portador'],
          ["[25,29]", doiscincodoisnoveP, doiscincodoisnoveI],
          ["[30,34]",treszerotresquatroP, treszerotresquatroI],
          ["[35,39]", trescincotresnoveP, trescincotresnoveI],
          ["[40,44]", quatrozeroquatroquatroP, quatrozeroquatroquatroI],
          ["[45,49]", quatrocincoquatronoveP, quatrocincoquatronoveI],
          ["[50,54]", cincozerocincoquatroP, cincozerocincoquatroI],
          ["[55,59]", cincocincocinconoveP, cincocincocinconoveI],
          ["[60,64]", seiszeroseisquatroP, seiszeroseisquatroI],
          ["[65,69]", seiscincoseinoveP, seiscincoseinoveI],
          ["[70,74]", setezerosetequatroP, setezerosetequatroI],
          ["[75,79]", setecincosetenoveP, setecincosetenoveI],
          ]
 tab = PrettyTable(table[0])
 tab.add_rows(table[1:])
 print(tab)


def calculaDistrsexo():


    mp = len(mydictionar["MP"])
    mi = len(mydictionar["MI"])
    fp =len(mydictionar["FP"])
    fi =len(mydictionar["FI"])


    table = [[' ', 'Masculino', 'Feminino'], ["Portador ", mp, fp], ["Não Portador ",mi, fi]]
    tab = PrettyTable(table[0])
    tab.add_rows(table[1:])
    print(tab)


def parser(name):

    #MP=MASCULINO PORTADOR DE DOENÇA
    mydictionar["MP"] = []
    mydictionar["FP"]=[]
    mydictionar["MI"] = []
    mydictionar["FI"] = []
    f = open("files/myheart.csv", "r")
    for i in f :
        k=i.split(",")
        #falta limpar os registos inválidos

        tuple = (k[0],k[2],k[3],k[4])
        if (k[1] == "M" and k[5].strip("\n") =="0"):
            mydictionar["MI"].append( tuple)
        if (k[1] == "M" and  k[5].strip("\n") == "1"):
            mydictionar["MP"].append( tuple)
        if (k[1] == "F" and k[5].strip("\n") =="0"):
            mydictionar["FI"].append( tuple)
        if (k[1] == "F" and  k[5].strip("\n") == "1"):
            mydictionar['FP'].append( tuple)

    # Use a breakpoint in the code line below to debug your script.
    f.close();

   # print(f'TPC1')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    opcao =1

    while (opcao!=4):
        print("-------------------TPC1-A96075--------------------------------")
        print("| 1-> Obter a distribuição da doença por sexo                |")
        print("| 2-> Obter a distribuição da doença por idade               |")
        print("| 3-> Obter a distribuição da doença por níveis de coleterol |")
        print("| 4->Sair                                                    |")
        print("--------------------------------------------------------------")
        opcao = input("Insira a opção que pretende realizar :\n")
        if (opcao =="1") :
            calculaDistrsexo()
        elif (opcao == "2"):
            calculaDistIdade()
        elif(opcao=="3"):
            calculadistrcolesterol()
        else :
            break




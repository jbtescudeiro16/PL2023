from turtle import pd

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

def parser():

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

  
    f.close();
#2time---------------------------------------------



def sexdist():
    masc = len(mydictionar["MP"])
    masc+= len(mydictionar["MI"])

    fem = len(mydictionar["FP"])
    fem += len(mydictionar["FI"])

    mp = len(mydictionar["MP"])
    mi = len(mydictionar["MI"])
    fp = len(mydictionar["FP"])
    fi = len(mydictionar["FI"])

    table = [[' ', 'Masculino', 'Feminino'], ["Portador ", mp, fp], ["Não Portador ",mi, fi],["TOTAL ",masc, fem]]
    tab = PrettyTable(table[0])
    tab.add_rows(table[1:])

    print(tab)

def ageinInterval(value,min,max):
    if (getage(value)>=min and getage(value)<=max) :
        return  True

    return False


def getpositives(min,max):
    count = 0
    for i in mydictionar["FP"]:
        if ageinInterval((i), min, max):
            count += 1
    for i in mydictionar["MP"]:
        if ageinInterval((i), min, max):
            count += 1
    return count
def getnegatives(min,max):
    count=0
    for i in mydictionar["FI"]:
        if ageinInterval((i),min,max):
            count+=1
    for i in mydictionar["MI"]:
        if ageinInterval((i),min,max):
            count+=1
    return count


def distidades():
 min=25

 table = [[' ', 'Portador', 'Não Portador']]

 while (min < 80):
        table.append([f"[{min},{min + 4}]", getpositives(min, min + 4 ),getnegatives(min, min + 4 )])

        min += 5
 tab = PrettyTable(table[0])
 tab.add_rows(table[1:])
 print(tab)




if __name__ == '__main__':
    opcao =1
    parser()
    while (opcao!=4):
        print("-------------------TPC1-A96075--------------------------------")
        print("| 1-> Obter a distribuição da doença por sexo                |")
        print("| 2-> Obter a distribuição da doença por idade               |")
        print("| 3-> Obter a distribuição da doença por níveis de coleterol |")
        print("| 4->Sair                                                    |")
        print("--------------------------------------------------------------")
        opcao = input("Insira a opção que pretende realizar :\n")
        if (opcao =="1") :
            sexdist()
        elif (opcao == "2"):

            distidades()
        elif(opcao=="3"):
            calculadistrcolesterol()
        else :
            break




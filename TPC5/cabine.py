import re


def cabine():
    possiveis=[
        r"LEVANTAR",
        r"POUSAR",
        r"T=[0-9]{9}",
        r"T=00[0-9]*",
        r"ABORTAR",
        r"MOEDA ((\d+)c|(\d+)e)*(, ((\d+)c|(\d+)e)*)*."
    ]
    #   r"MOEDA ((1|2|5|10|20|50)c|(1|2)e)*(, ((1|2|5|10|20|50)c|(1|2)e)*)*."
    state=0
    nrTlm=0
    saldo=0.00
    custo = 0.00
    moedas=[]
    while state!=-1 :
        i=input()
        re.sub(r"\n","",i)
        if (re.fullmatch(r"|".join(possiveis),i))!=None:
             if i=="LEVANTAR":
                 if state==0:
                    state=1
                    print("Introduza Moedas")
                 elif state==1:
                     print("Telefone já levantado!")
                 elif state==2:
                     print("Impossível levantar!Chamada em Curso.")

             elif i=="POUSAR":
                 if state==0:
                     print("telefone nao levantado")
                     state=0
                 elif (state==2):
                     print("Saldo inicial: "+str(saldo)+"€.")
                     print("Chamada terminada com um custo de: " +str(custo) +" €.")
                     print("Chamada terminada com um custo de: " + str(custo) + " €")
                     lolas=saldo-custo
                     print("Saldo devolvido " + str(lolas) + " €")
                     state=-1
                 elif(state==1):
                     print("Saldo devolvido " + str(saldo) + " €")
                     state=-1

             elif i=="ABORTAR":
                 print("O valor devolvido pela máquina é:"+str(saldo))
                 state=-1

             elif re.match(r"MOEDA",i):
                 if state==1:
                     moedas=[]
                     #nao esta a apanhar o c e devia
                     gex = r"(\d+(?:\.\d+)?[ce])";
                     b=re.findall(gex,i)
                     for valor in b:
                         if (re.match(r"((1|2|5|10|20|50)c|(1|2)e)",valor)!=None):
                            moedas.append(valor)

                         else :
                             print("Moeda "+valor+" invalido")
                     for valor in moedas:
                         if re.match(r"(1|2|5|10|20|50)c",valor):

                            a=re.findall(r"(10|20|50)",valor)
                            if a!=[]:

                                saldo+= (float)(a[0])*0.01
                                #print(saldo)
                            else:
                                b=re.findall(r"(1|2|5)",valor)
                                if b != []:

                                    saldo += (float)(b[0]) * 0.01

                                    #print(saldo)

                         else :
                            if re.search("(1|2e)",valor):
                                aux=re.findall(r"(1|2)e",valor)
                                saldo+=(int)(aux[0])
                     format_float = "{:.2f}".format(saldo)
                     print("O SEU SALDO É :" + format_float)
                 elif (state==2) :
                    print("Impossível introduzir moeda ! Chamada em Curso.")
                 elif (state == 0):
                     print("Impossível introduzir moeda ! Telefone não levantado")
             elif re.match(r"T=", i):
                 if state==1:
                     if re.match("T=(601|641)",i):
                         print("JF no número")
                         state=-1

                     if re.match("T=00",i):
                         if saldo>=1.5:
                             format_float = "{:.2f}".format(saldo)
                             print("O SEU SALDO É :" + format_float)
                             print("Chamada iniciada para o número: "+i)
                             custo+=1.5
                             state=2
                         else:
                             print("Saldo insuficiente, por favor insira moedas")
                             state = 1
                     if re.match("T=2",i):
                         if saldo>=0.5:
                             format_float = "{:.2f}".format(saldo)
                             print("O SEU SALDO É :" + format_float)
                             print("Chamada iniciada para o número: " + i)
                             custo+=0.25
                             state=2
                         else:
                             print("Saldo insuficiente,por favor introduza moedas")
                             state = 1
                     if re.match("T=800", i):
                             format_float = "{:.2f}".format(saldo)
                             print("O SEU SALDO É :" + format_float)
                             print("Chamada iniciada para o número: " + i)
                             custo += 0
                             state = 2
                     if re.match("T=808",i):
                         if saldo>=0.1:
                             format_float = "{:.2f}".format(saldo)
                             print("O SEU SALDO É :" + format_float)
                             print("Chamada iniciada para o número: " + i)
                             custo+=0.10
                             state=2
                         else:
                             print("Saldo insuficiente,por favor introduza moedas")
                             state = 1

                 else :
                     print("Telefone nao levantado")





if __name__ == '__main__':
     cabine()
import json
import re


informacao=[]
def aux ():
    parametros = []
    flagarray = 0
    flagspace = []
    function = None

    f=open("file/alunos.csv",encoding="utf-8")
    i=0
    for l in f :
       if (i ==0):

           parametros =re.split(",",re.sub(r"{(\d+),(\d+)}",r"{\1;\2}",l.strip("\n")))
       i+=1
    f.close()
    for i in parametros:

        if (re.search("\{\d+\}", i)):
            flagarray=int(re.findall("\d+",i)[0])

        if flagarray==0:
                aux = re.findall(r";(\d+)}",i)
                if aux==[]:flagarray=0
                else :flagarray=int ((re.findall(r";(\d+)}",i))[0])

                # print(flagspace)
            #print("flagarray"+str(flagarray))


        if re.search(r"::sum", i):

                function = "sum"

        if re.search(r"::media", i):

                function = "media"


    #print(function)
    #print(parametros)

    #---------------Variaveis jja cheias
    print("encher")
    f = open("file/alunos.csv", encoding="utf-8")

    i=0

    linhaseparada=""
    for line in f :
        flag=False
        indice = 0
        dicionario = dict()
        if i!=0:
            linhaseparada=re.split(r",",line.strip("\n"))

            i+=1

            for pos in parametros:

                if pos =="":continue

                if flagspace==[] and flagarray==0:
                    dicionario[pos] = linhaseparada[indice]
                    indice += 1

                elif flagarray!=0 :

                    if re.search(r"\d+",pos) or flag==True:
                        flag=True
                        array = []

                        for i in range(0, flagarray):
                            value = linhaseparada[indice]

                            indice += 1

                            if (value != ''):
                                array.append(int(value))

                            if function == None:
                                dicionario[pos] = array

                            else:
                                field_name = pos.split("{")[0] + "_" + function

                                _sum = 0

                                for array_value in array:
                                    _sum += array_value

                                if function == "sum":

                                    dicionario[field_name] = _sum

                                elif function == "media":

                                    dicionario[field_name] = _sum / len(array)




                    elif  flag==False:
                        dicionario[pos] = linhaseparada[indice]
                        indice += 1



            informacao.append(dicionario)
        i+=1
    f.close()
    f.close()

    json_string = json.dumps(informacao, ensure_ascii=False, indent=2)

    f = open("output.json", "w", encoding="utf8")

    f.write(json_string)

    f.close()
   #print(informacao)





if __name__ == '__main__':
    aux()



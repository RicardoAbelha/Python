#Faça um Programa que peça uma data no formato dd/mm/aaaa 
# e determine se a mesma é uma data válida.
print("digita uma data valida, no formato XX/XX/XXX)
dia = int(input("Digite o dia: "))

#print(dia,"/",mes,"/",ano)
if dia <= 1 or dia >=31: 
    print("valor do dia não confere")
    dia = int(input("Digite uma nova data: "))
    if dia >= 1 or dia <=31: 
        mes = int(input("Digite o mes: "))
        if mes <= 1 or mes >=12:
            print("valor do mes não confere")
            mes = int(input("Digite uma nova valor: "))
            if mes >= 1 or mes <= 12:
                ano = int(input("Digite o ano: "))
                print(dia,"/",mes,"/",ano)
                print("A data é valida!")
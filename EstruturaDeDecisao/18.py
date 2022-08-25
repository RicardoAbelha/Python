# Faça um Programa que peça uma data no formato dd/mm/aaaa
# e determine se a mesma é uma data válida.
print("digita uma data valida, no formato XX/XX/XXXX")
dia = int(input("Digite o dia: "))

# print(dia,"/",mes,"/",ano)
if dia <= 1 and dia >= 31:
    print("valor do dia não confere")
    dia = int(input("Digite uma nova data: "))

mes = int(input("Digite o mes: "))
if mes <= 1 and mes >= 12:
    print("valor do mes não confere")
    mes = int(input("Digite uma nova valor: "))

ano = int(input("Digite o ano: "))
if ano >= 1 and ano <= 9999:
    print(dia, "/", mes, "/", ano)
    print("A data é valida!")
else:
    print("data invalida!")

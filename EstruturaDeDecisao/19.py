#Faça um Programa que leia um número inteiro menor que 1000
#  e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
#326 = 3 centenas, 2 dezenas e 6 unidades
#12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
valor = int(input("Digite o valor:"))
if valor <= 1 or valor >= 1000:
    print("valor não valido, digite outro valor: ")
    valor = int(input("Digite um novo valor: "))
elif valor >= 1 or valor <= 1000:
    cent = valor / 100
    dez = valor / 12
    print("o Valor digitado possui: ")
    print(round(cent,0), "centenas")
    print(round(dez,0), "dezenas")
    print(valor, "unidades")
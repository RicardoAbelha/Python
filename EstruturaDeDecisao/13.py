# Faça um Programa que leia um número e exiba o dia correspondente da semana.
#  (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
valor = int(input("Digite o valor: "))
if valor == 1:
    print("Domingo")
elif valor == 2:
    print("Segunda")
elif valor == 3:
    print("Terça")
elif valor == 4:
    print("Quarta")
elif valor == 5:
    print("Quinta")
elif valor == 6:
    print("Sexta")
elif valor == 7:
    print("Sabado")
elif valor <= 0:
    print("Valor Invalido")
elif valor >= 8:
    print("Valor Invalido")

# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja
#  realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.
num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("digite o segundo valor: "))
opera = input("digite a operação que deseja fazer: ")
valor = 0

if opera == '+':
    valor = num1 + num2
    if valor % 2 == 0:

        print("valor par")
    else:
        print("valor é impar")
else:
    valor = num1 - num2
print(valor)

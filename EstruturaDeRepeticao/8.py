# Faça um programa que leia 5 números e informe a soma e a média dos números.
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))
num3 = int(input("Digite o terceiro numero: "))
num4 = int(input("Digite o quarto numero: "))
num5 = int(input("Digite o quinto numero: "))

soma = (num1 + num2 + num3 + num4 + num5)
media = (soma / 5)

print(num1, num2, num3, num4, num5)
print(soma)
print(media)
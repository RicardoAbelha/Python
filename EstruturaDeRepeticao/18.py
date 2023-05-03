# Faça um programa que, dado um conjunto de N números, 
# determine o menor valor, o maior valor e a soma dos valores.

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))
#num4 = int(input("Digite um numero: "))

soma = num1 + num2 + num3

print(num1, num2, num3)

print(soma)


print('')
print('Analisando os números...')
print('')
if num1 > num2 and num3:
    maior = num1
if num2 > num1 and num3:
    maior = num2
if num3 > num1 and num2:
    maior = num3
if num1 < num2 and num3:
    menor = num1
if num2 < num1 and num3:
    menor = num2
if num3 < num1 and num2:
    menor = num3
print(f'O maior número é {maior}.')
print('')
print(f'E o menor número é {menor}.')
print(menor)
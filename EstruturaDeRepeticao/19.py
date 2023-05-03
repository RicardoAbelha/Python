# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.


num1 = int(input("Digite um numero: "))
num2 = int(input("Digite um numero: "))
num3 = int(input("Digite um numero: "))

if not 1 <= num1 <= 1000:
    print('O numero deve ser entre 1 e 1000')
    
if not 1 <= num2 <= 1000:
    print('O numero deve ser entre 1 e 1000')
    
if not 1 <= num3 <= 1000:
    print('O numero deve ser entre 1 e 1000')
    
    
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
# Elabore um programa que receba um inteiro entre 0 e 8 (não aceitar valores fora dessa faixa)
# e calcule o fatorial do número dado.

numero = int(input("Digite o Numero: "))

if numero < 0 or numero > 8:
    print("Numero fora do espctro")
    numero = int(input("Digite o Numero: "))

resultado = 1
count = 1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)

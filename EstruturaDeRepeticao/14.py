# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

pares = 0
impares = 0
for numero in range(1,11):
    inteiro = int(input("Insira um número inteiro:"))
    if inteiro % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
        
print("A quantidade de números pares é: ", pares)
print("A quantidade de números ímpares é: ", impares)
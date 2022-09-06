# Elabore um programa que some os nprimeiros números ímpares, utilizando while. Por exemplo,
# para n = 5: 1 + 3 + 5 + 7 + 9 = 25.

controle = 0
numero = 0
soma = 0
numero = int(input("Digite um numero: "))

while controle > numero:
    if controle % 2 != 0:
        soma = soma + controle
        controle = controle + 1

print(soma)
print(numero)

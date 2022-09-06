# Escreva um programa que faça a soma de todos os números menores ou iguais a 50
# que são múltiplos de 3 ou 5. Utilize um laço do tipo whilepara realizar a tarefa.
# Qual operador aritmético iremos utilizar para definir se um número é múltiplo de 3 ou 5?

soma = int(0)
for M3 in range(0, 50):
    if (M3 % 3 == 0):
        soma = M3 + soma
        M3 = M3 + 1

print(M3)
print(soma)

soma = int(0)
for M5 in range(0, 50):
    if (M5 % 5 == 0):
        soma = M5 + soma
        M5 = M5 + 1

print(M5)
print(soma)

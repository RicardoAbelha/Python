# (35 pontos) Escreva um programa que leia do usuário um número inteiro, maior que 1,
# e imprima o enésimo número da sequência de Fibonacci. Os dois primeiros termos dessa
# sequência são sempre 0 e 1. A partir de seu terceiro elemento, ele é calculado pela soma dos dois anteriores, de maneira que fib(n) = fib(n-1) + fib(n-2).
# Por exemplo, os dez primeiros termos da sequência são: 0, 1, 1, 2, 3, 5, 8, 13, 21 e 34.
# Se o usuário entrar com o número 11, qual seria a resposta do programa?
# Dica: Declare, também, variáveis inteiras para guardar os dois números anteriores e as inicialize com 0 e 1.
# Depois, faça um laço for que comece no terceiro elemento e vá calculando até o elemento n desejado

termos = int(input("Digite a quantidade de termos para calcular : "))
if termos >= 1:
    num1, num2 = 0, 1
    contador = 0
    while contador < termos:
        num3 = num1 + num2

        num1 = num2
        num2 = num3
        contador += 1
        print(num1)
print(num1)
print(contador)

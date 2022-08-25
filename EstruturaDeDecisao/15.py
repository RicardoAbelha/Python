# Faça um Programa que peça os 3 lados de um triângulo.
#  O programa deverá informar se os valores podem ser um triângulo.
#  Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;
lado1 = int(input("Digite um lado: "))
lado2 = int(input("Digite o outro lado:"))
lado3 = int(input("Digite o terceiro lado: "))
if (lado1 + lado2) < lado3:
    print("Não é Triangulo")
elif lado1 == lado2 and lado2 == lado3 and lado1 == lado3:
    print("Triângulo Equilátero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Triângulo Isósceles")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("Triângulo Escaleno")

print("Digite tres valores do triangulo")
ladoA = float(input("Digite o primeiro valor: "))
ladoB = float(input("Digite o segundo valor: "))
ladoC = float(input("Digite o terceiro valor: "))

if (ladoA + ladoB >= ladoC) or (ladoA + ladoC >= ladoB) or (ladoB + ladoC >= ladoA):
    print("Os valores não correspondem a um triangulo")
else:
    if ladoA == ladoB and ladoA == ladoC:
        print("É triangulo Equilátero")
    if (ladoA == ladoB and ladoB != ladoC) or (ladoA == ladoC and ladoA != ladoB) or (ladoA != ladoB and ladoB == ladoC):
        print("É triangulo Equilátero Isósceles")
    if ladoA != ladoB and ladoA != ladoC and ladoB != ladoC:
        print("É triangulo Equilátero Escaleno")

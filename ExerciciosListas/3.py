#3.	Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

nota1 = int(input("Digite a nota 1: "))
nota2 = int(input("Digite a nota 2: "))
nota3 = int(input("Digite a nota 3: "))
nota4 = int(input("Digite a nota 4: "))

print(nota1)
print(nota2)
print(nota3)
print(nota4)

soma = nota1 + nota2 + nota3 + nota4

print(soma)

media = float(nota1 + nota2 + nota3 + nota4)/4

print(media)

if (media >= 7):
    print("Você foi aprovado!")
else:
    print("Estude mais!!")
#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
#  e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#  Média de Aproveitamento  Conceito
#  Entre 9.0 e 10.0        A
#  Entre 7.5 e 9.0         B
#  Entre 6.0 e 7.5         C
#  Entre 4.0 e 6.0         D
#  Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média,
#  o conceito correspondente e a mensagem “APROVADO” 
# se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = float((nota1 + nota2)/2)
if media >= 9.0 and media <= 10.0:
    print("Suas notas foram: ", nota1,  " " , nota2)
    print("Sua media foi: ", media)
    print("Seu conceito foi: A")
    print("Você foi Aprovado")
elif media >= 7.5 and media <= 9.4:
    print("Suas notas foram: ", nota1,  " " , nota2)
    print("Sua media foi: ", media)
    print("Seu conceito foi: B")
    print("Você foi Aprovado")
elif media >= 6.0 and media <= 7.4:
    print("Suas notas foram: ", nota1,  " " , nota2)
    print("Sua media foi: ", media)
    print("Seu conceito foi: C")
    print("Você foi Aprovado")
elif media <= 4.0 and media >= 5.9:
    print("Suas notas foram: ", nota1,  " " , nota2)
    print("Sua media foi: ", media)
    print("Seu conceito foi: D")
    print("Você foi Reprovado")
elif media <= 3.9 and media >= 0:
    print("Suas notas foram: ", nota1,  " " , nota2)
    print("Sua media foi: ", media)
    print("Seu conceito foi: E")
    print("Você foi Reprovado")

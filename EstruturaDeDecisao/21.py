# Faça um Programa para um caixa eletrônico.
#  O programa deverá perguntar ao usuário a valor do saque e depois
#  informar quantas notas de cada valor serão fornecidas.
#  As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
#  O valor mínimo é de 10 reais e o máximo de 600 reais.
#  O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
print("Olá, bem vindo ao caixa eletronico!")
valor = int(input("qual valor desejado: "))
if valor <= 9 and valor >= 601:
    print("valor fora da possibilidade de transação:")
    valor = int(input("Digite o valor: "))
    if valor >= 10 or valor <= 600:
        cent = valor / 100
        cinq = valor / 50
        dez = valor / 10
        unid = valor
        print("o valor do saque: ")
        print(cent, "notas de 100")
        print(dez, "notas de 50")
        print(unid, "valor de 1")

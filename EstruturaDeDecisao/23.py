# Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
#  Dica: utilize uma função de arredondamento.
valor = float(input("Digite o valor: "))

if(round(valor) == True):
    print(f'{int(valor)} é um número inteiro!')
else:
    print(f'{valor} é um número decimal!')

print("Arredondado    :", round(valor))

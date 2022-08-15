#Faça um programa que leia 5 números e informe o maior número.
num1 = input("Digite o primeiro numero: ")
while num1 == 0 or num1 == "":
    num1 = input("Digite o primeiro numero: ")
num2 = input("Digite o segundo numero: ")
while num2 == 0 or num2 == "" or num2 == num1:
    num2 = input("Digite o segundo numero: ")
num3 = input("Digite o terceiro numero: ")
while num3 == 0 or num3 == "" or num3 == num1 or num3 == num2:
    num3 = input("Digite o terceiro numero: ")
num4 = input("Digite o quarto numero: ")
while num4 == 0 or num4 == "" or num4 == num1 or num4 == num2 or num4 == num3:
    num4 = input("Digite o quarto numero: ")
num5 = input("Digite o quinto numero: ")
while num5 == 0 or num5 == "" or num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
    num5 = input("Digite o quinto numero: ")
    
if num1 > num2 or num1 > num3 or num1 > num4 or num1 > num5:
    print(num1)
elif num2 > num1 or num2 > num3 or num2 > num4 or num2 > num5:
    print(num2)
elif num3 > num1 or num3 > num2 or num3 > num4 or num3 > num5:
    print(num3)
elif num4 > num1 or num4 > num2 or num4 > num3 or num4 > num5:
    print(num4)
elif num5 > num1 or num5 > num2 or num5 > num3 or num5 > num4:
    print(num5)
        
print(num1, num2, num3, num4, num5)


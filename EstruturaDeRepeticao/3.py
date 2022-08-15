#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';
nome = input("Nome: ")
while len(nome) < 3:
    nome = input("Digite nome valido: ")
     
idade = int(input("Idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Digite idade valida: "))

salario = float(input("Salário: "))
while salario < 0:
    salario = float(input("Salário não pode ser 0: "))

sexo = input("Sexo: ")
while sexo != "F" and sexo != "f" and sexo != "M" and sexo != "m":
    sexo = input("Digite o sexo: ")
 
estado_civil = input("Estado Civil: ")
while estado_civil != "S" and estado_civil != "s" and estado_civil != "C" and estado_civil != "c" and estado_civil != "V" and estado_civil != "v" and estado_civil != "D" and estado_civil != "d":
    sexo = input("qual o Estado Civil: ")
    
print(nome)
print(idade)
print(salario)
if sexo == "M" or sexo == "m":
    print("Masculino")
elif sexo == "F" or sexo == "f":
    print("Feminino")
    
if estado_civil == "S" or estado_civil == "s":
    print("Solteiro")
elif estado_civil == "C" or estado_civil == "c":
    print("Casado")
elif estado_civil == "V" or estado_civil == "v":
    print("Viuvo")
elif estado_civil == "D" or estado_civil == "d":
    print("Divorciado")
#Altere o programa anterior permitindo ao usuário informar
#  as populações e as taxas de crescimento iniciais.
#  Valide a entrada e permita repetir a operação.
cidadeA = int(input("Digite a população da primeira cidade: "))
while cidadeA == 0 or cidadeA == "":
    cidadeA = int(input("Digite a população da primeira cidade: "))
cidadeB = int(input("Digite a população da segunda cidade: "))
while cidadeB == 0 or cidadeB == "":
    cidadeA = int(input("Digite a população da segunda cidade: "))

cresA = float (input("Digite a taxa de crescimento da primeira cidade: "))
while cresA == 0 or cresA == "":
    cresA = float (input("Digite a taxa de crescimento da primeira cidade: "))
cresB = float (input("Digite a taxa de crescimento da primeira cidade: "))
while cresB == 0 or cresA == "":
    cresB = float (input("Digite a taxa de crescimento da primeira cidade: "))
    


anos = 0

while (cidadeA < cidadeB):
    anos += 1
    cidadeA = cidadeA + (cidadeA * cresA)
    cidadeB = cidadeB + (cidadeB * cresB)
print("Após %i anos o país A ultrapassou o país B em número de habitantes." % anos)
print("País A: %.0f" % cidadeA)
print("País B: %.0f" % cidadeB)

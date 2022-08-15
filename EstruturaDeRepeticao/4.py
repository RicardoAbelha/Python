#Supondo que a população de um país A seja da ordem de 80000 habitantes
#  com uma taxa anual de crescimento de 3% e que a população de B seja 
# 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa
#  que calcule e escreva o número de anos necessários para que a população 
# do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
cidadeA, cidadeB, anos = 80000, 200000, 0
cresA, cresB = 0.03, 0.015 # Crescimentos de 3% e 1,5% ao ano
while (cidadeA < cidadeB):
    anos += 1
    cidadeA = cidadeA + (cidadeA * cresA)
    cidadeB = cidadeB + (cidadeB * cresB)
print("Após %i anos o país A ultrapassou o país B em número de habitantes." % anos)
print("País A: %.0f" % cidadeA)
print("País B: %.0f" % cidadeB)

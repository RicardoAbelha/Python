# Faça um programa que contenha uma lista para cada atributo pessoal como a cor dos olhos
# (A -Azul, P -Preto, V -Verde e C -Castanho) e a cor dos cabelos (P -Preto, C -Castanho, L -Louro e R -Ruivo)
# e a etnia(Africano, Português, Índio e Holandês). Você deve usar aninhamento para fazer todas as combinações
# possíveis entre os atributos, uma combinação seria:
# O Holandês possui cabelo Ruivo e olhos castanhos.
#

corOlhos = ["Azul", "Preto", "Verde", "Castanho"]
corCabelo = ["Preto", "Castanho", "Louro", "Ruivo"]
etinia = ["Africano", "Portugues", "Indio", "Holandes"]

for x in corOlhos:
    for y in corCabelo:
        for z in etinia:
            print("O " + z + " possui cabelo " +
                  y + " e olhos " + x)

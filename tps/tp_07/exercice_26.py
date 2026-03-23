# Exercice 26 : Ecrire un programme qui simule 1000 lancers d'un dé, stocke les résultats dans une liste, trie la liste par ordre décroissant, puis compte le nombre de 6 obtenus sans parcourir entièrement la liste, puis affiche le nombre de 6.

import random

nbrdes = 1000

def generate_nbr():
    nbr = random.randint(1, 6)
    return nbr

list = []

for i in range(0, nbrdes):
    list.append(generate_nbr())

list.sort(reverse=True)

indexdes = 0
nbr_six = 0


while(list[indexdes] == 6):
    nbr_six += 1
    indexdes += 1

print(list)
print(f"{nbr_six} , semble normal car 1000/6 = {1000/6}")
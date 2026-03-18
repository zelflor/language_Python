# Exercice 12 : Ecrire un programme qui affiche le numéro d'un département de la région Centre choisi au hasard.

# Remarque : cet exercice porte sur la génération de nombres aléatoires avec randint et non sur la génération d'une liste en compréhension.

from random import *

list_departement = [28, 45, 41, 37, 36, 18]
departement = randint(0,5)

print(list_departement[departement])
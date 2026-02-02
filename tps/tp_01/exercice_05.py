# Exercice 5 : Simuler le lancer de deux dés et afficher la somme obtenue. 

from random import *

de1 = randint(1, 6)
de2 = randint(1, 6)

print("Lancement du premier dè ...")
print(de1)

print("Lancement du deuxieme dè ...")
print(de2)

sommedes = de1 + de2

print("Somme des deux des : ", sommedes ," ")
# Exercice 12 : Ecrire un programme qui simule 1000 lancers de deux dés, et qui affiche le nombre de fois où une somme comprise entre 4 et 8 inclus a été obtenue. 

from random import *


compteur = 0


for i in range(1000):
    dé = randint(1,6)
    dé2 = randint(1,6)
    if (dé + dé2 >= 4 and dé + dé2 <= 8):
        compteur +=1
print("La somme entre 4 et 8 est sorti",compteur,"fois.")
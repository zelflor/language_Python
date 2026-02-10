# Exercice 6 : Ecrire un programme qui simule 1000 lancers de deux dés, et qui affiche le nombre de fois où la somme 10 a été obtenue. 
from random import *


compteur = 0


for i in range(1000):
    dé = randint(1,6)
    dé2 = randint(1,6)
    if (dé + dé2 == 10):
        compteur +=1
print("Le résultat 10 est sorti",compteur,"fois.")
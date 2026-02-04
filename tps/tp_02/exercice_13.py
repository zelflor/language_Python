from random import *

somme = 0
for i in range(1000):
    de = randint(1, 6)
    somme = somme + de

somme = somme / 1000

print(somme)


# Exercice 2 : Reprendre l'exercice 6 du chapitre 5 sans utiliser de boucle while :
# Ecrire un programme qui demande à l'utilisateur de saisir un nombre entier strictement positif et qui affiche le nombre de chiffres de ce nombre. 

nbr = -1

while nbr < 0:
    nbr = int(input("Entrez un nombre : "))

nbr = str(nbr)
nbrsize = len(nbr)

print(nbrsize)
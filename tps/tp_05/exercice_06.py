# Exercice 6 : Ecrire un programme qui demande à l'utilisateur de saisir un nombre entier strictement positif et qui affiche le nombre de chiffres de ce nombre.
# Votre programme doit utiliser une boucle while. 
nbr = -1

while nbr < 0:
    nbr = int(input("Entrez un nombre : "))

nbr = str(nbr)
nbrsize = len(nbr)

print(nbrsize)
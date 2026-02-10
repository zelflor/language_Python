# Exercice 3 : Ecrire un programme qui demande à l'utilisateur de saisir un nombre (positif ou négatif), puis qui affiche la valeur absolue de ce nombre. 

nbr = int(input('Entrez un nombre : '))

if (nbr < 0):
    print(abs(nbr))
else:
    print(nbr)
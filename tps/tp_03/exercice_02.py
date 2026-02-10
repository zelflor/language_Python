# Exercice 2 : Ecrire un programme qui demande à l'utilisateur de saisir deux nombres, puis qui affiche le plus grand de ces deux nombres. 
nbr1 = int(input("Entrer le nombre 1 : "))
nbr2 = int(input("Entrer le nombre 2 : "))

if (nbr1 > nbr2):
    print(nbr1)
else:
    print(nbr2)
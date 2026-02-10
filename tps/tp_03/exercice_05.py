# Exercice 5 : Réécrire le programme qui affiche la plus grande des deux valeurs saisies par l'utilisateur, mais cette fois sans utiliser la clause else. 

nbr1 = int(input("Entrez le nombre 1 : "))

nbr2 = int(input("Entrez le nombre 2 : "))


if (nbr1 > nbr2):
    nbr2 = nbr1

print(nbr2)
# Exercice 6 : Ecrire un programme qui demande à l'utilisateur de saisir un mot, et qui affiche ce mot verticalement (sur une colonne). 

saisie = input("Entrez un mot : ")

taillesaisie = len(saisie)

i = 0

while i < taillesaisie:
    print(saisie[i])
    i += 1
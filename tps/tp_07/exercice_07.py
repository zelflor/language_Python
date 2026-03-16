# Exercice 7 : Ecrire un programme qui :

#     initialise une liste de longueur 10 avec des 0
#     demande à l'utilisateur de saisir un emplacement entre 0 et 9
#     écrit dans la liste la valeur 1 à l'emplacement choisi par l'utilisateur
#     affiche la liste complète


liste = [0] * 10


emplacement = -1
while (emplacement < 0 or emplacement >= 10):
    emplacement = int(input("Saisir un emplacement de 0 et 9 : "))

liste[emplacement] = 1

print(liste)
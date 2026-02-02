# Exercice 11 : Ecrire un programme qui demande à l'utilisateur d'entrer le rayon d'un cercle et qui affiche son périmètre.
# Le programme doit fonctionner pour des valeurs non entières du rayon, et devra afficher une phrase de réponse complète se terminant par un point. 
from math import pi

rayon_cercle = float(input("Entrez le rayon du cercle : "))


perimetre = pi * rayon_cercle * 2

print(f"Le perimetre de ce cercle est {perimetre}")
# Exercice 5 : Le jeu "Plus ou Moins"
# Programmer le jeu suivant :
# L'ordinateur choisi un nombre entier aléatoire entre 1 et 100.
# Le joueur doit deviner ce nombre-mystère en faisant plusieurs propositions successives. Après chaque proposition, le programme indique au joueur si son nombre est trop petit ou trop grand. Le jeu s'arrête lorsque le nombre-mystère a été trouvé.
# Vous pouvez ajouter un compteur qui indique le nombre d'essais du joueur.
# Question subsidiaire : Quel nombre minimal d'essais faut-il faire pour être sûr de deviner le nombre?
import random

nbr_random = int(random.randint(1, 100))
nbr_entrer = 0
while nbr_random != nbr_entrer:
    if (nbr_entrer < nbr_random):
        print("Le nombre est plus grand")
    else:
        print("Le nombre est plus petit")
    nbr_entrer = int(input("Entrez un nombre : "))
print(f"Vous avez trouver le nombre {nbr_random}")
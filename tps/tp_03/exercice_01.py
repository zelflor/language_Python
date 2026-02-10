# Exercice 1 : Il faut mesurer au moins 1m30 pour pouvoir entrer dans un parc d'attractions.
# Ecrire un programme qui demande à l'utilisateur sa taille en cm, et qui lui indique s'il peut ou non rentrer dans le parc. 

taille_cm = int(input("Entrez votre taille en cm : "))

if (taille_cm >= 130):
    print("Vous pouvez entrer dans le parc d'attractions")
else:
    print("Vous ne pouvez pas entrer dans le parc d'attractions (plus ou egal a 1m30)")
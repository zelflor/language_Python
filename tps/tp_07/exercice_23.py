# Exercice 23 : Quel est le rôle de l'algorithme ci-dessous?
# Indication : vous pouvez faire des essais en modifiant la liste de la première ligne.

liste = [5,8,1,9,7,6]
for i in range(len(liste)):
    for j in range(len(liste)-1):       
        if liste[j] > liste[j+1]:
            aux = liste[j]
            liste[j] = liste[j+1]
            liste[j+1] = aux
print(liste)

# Il permet de mettre par ordre croissant les chiffres dans la listes
# Exercice 22 : Ecrire un programme qui entrelace les deux listes liste1 et liste2.
# Plusieurs méthodes sont possibles.

liste1 = [4,8,6,0,6,4]
liste2 = [5,1,9,3,7,3]

listeSomme = []


for a,b in zip(liste1,liste2):
    listeSomme.append(a)
    listeSomme.append(b)

print(listeSomme)
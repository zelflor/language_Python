# Exercice 21 : Ecrire un programme qui utilise la fonction zip pour calculer la moyenne pondérée des notes ci-dessous. Les coefficients de chaque note sont donnés dans une liste de même taille.


notes = [6,9,10,14,13]
coefficients = [2,1,4,3,2]
listeSomme = []
for a,b in zip(notes,coefficients):
    listeSomme.append(a * b) 
print(listeSomme)


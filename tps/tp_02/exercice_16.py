# Exercice 16 : Quel est le rôle de l'algorithme ci-dessous ?

a = float(input("Veuillez saisir un nombre positif (pas nécessairement entier) : "))
r = 1
for i in range(20):
   r = r / 2 + a / r / 2
print(r)


# Cette algorithme permet d'obtenir la racine du nombre float a
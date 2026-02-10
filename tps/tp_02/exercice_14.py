# Exercice 14 : Ecrire un programme qui demande à l'utilisateur un entier a et un entier n et qui calcule 𝑎𝑛 à l'aide d'une boucle for (on verra plus tard un algorithme plus rapide que celui-ci).
# Remarque : il est interdit d'utiliser ** ici! 

entier = int(input("Entrez un entier : "))
puissance = int(input("Entrez la puissance : "))

for i in range(1, puissance):
    entier *= entier

print(entier)
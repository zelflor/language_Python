# Exercice 10 : Quelle est la valeur de la variable somme après exécution du programme ci-dessous ?
somme = 0
for i in range(10):
    somme = somme + i
    if i == 5:
        break

print(somme)
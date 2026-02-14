# Exercice 13 : Reprendre le problème des années bissextiles (exercice 11) en utilisant des opérateurs booléens à la place des conditions imbriquées.
# Une année est bissextile si elle est multiple de 4 mais pas multiple de 100, ou si elle est multiple de 400.
# Tester ensuite votre programme avec les années 2021, 2020, 1900 et 2000. 

annee = int(input("Veuillez saisir une année : "))

bissextile = (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

if bissextile:
    print(f"L'année {annee} est bissextile")
else:
    print(f"L'année {annee} n'est pas bissextile")
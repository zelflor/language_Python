# Exercice 15 : Ecrire un programme qui demande de saisir un entier positif n et qui calcule la factorielle de n.
# La factorielle de n, notée 𝑛! est définie par 𝑛!=1×2×3×...×𝑛 .
# On a par exemple 3!=6.

nombre = int(input("quelle est le nombre : "))

if (nombre == 0):
    print(1)
else:
    for i in range (1, nombre):
        nombre = nombre * i

    print(nombre)
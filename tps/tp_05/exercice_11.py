# Exercice 11 : Ecrire un programme qui affiche la liste de tous les nombres premiers compris entre 1 et 100.*


def ispremier(n):
    i = 2
    while i < n:
        if (n % i == 0):
            return False
        i += 1
    return True


for y in range(2, 100):
    if (ispremier(y)):
        print(y)

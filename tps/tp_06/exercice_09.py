# Exercice 9 : Reprendre l'exercice 8 en utilisant la syntaxe raccourcie. 


def nbOccurences(lettre, message):
    nbr = 0
    for i in message:
        if (lettre == i):
            nbr += 1
    return nbr

print(nbOccurences('a', 'abracadabra'))
print(nbOccurences('A', 'abracadabra'))

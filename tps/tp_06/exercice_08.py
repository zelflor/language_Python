# Exercice 8 : Ecrire une fonction nbOccurences(lettre, message) qui renvoie le nombre d'occurences d'une lettre (ou d'un caractère) dans un message. 

def nbOccurences(lettre, message):
    taillemessage = len(message)

    nbrlettre = 0
    i = 0
    while i < taillemessage:
        if (message[i] == lettre):
            nbrlettre += 1
        i += 1
    return nbrlettre

print(nbOccurences('a', 'abracadabra'))
print(nbOccurences('A', 'abracadabra'))

assert(nbOccurences('a', 'abracadabra') == 5)
assert(nbOccurences('A', 'abracadabra') == 0)
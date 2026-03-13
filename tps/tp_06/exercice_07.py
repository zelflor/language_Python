# Exercice 7 : Ecrire une fonction estPrésent(lettre, message) qui renvoie True ou False selon que la lettre est présente ou non dans le message.

def estPrésent(lettre, message):
    taillemessage = len(message)
    
    i = 0
    while i < taillemessage:
        if (message[i] == lettre):
            return True
    return False

assert(estPrésent('a', 'abracadabra') == True)
assert(estPrésent('r', 'abracadabra') == True)
assert(estPrésent('R', 'abracadabra') == False)
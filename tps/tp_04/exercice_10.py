# Exercice 10 : Expliquer dans quel cas on peut se passer d'évaluer la condition B dans l'expression A or B. 
# Ecrire ensuite un programme qui permet de vérifier l'évaluation paresseuse de l'opérateur booléen or.

def grand(taille):
    print("Dans la fonction grand()")
    return taille>180

def géant(taille):
    print("Dans la fonction géant()")
    return taille>190


taille = 200
print(grand(taille) or géant(taille))
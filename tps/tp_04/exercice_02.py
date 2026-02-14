# Exercice 2 : Ecrire une fonction périmètre qui prend en paramètre le côté d'un carré et qui renvoie le périmètre du carré correspondant.
# Faire ensuite un appel de cette fonction afin d'afficher le périmètre d'un carré de côté 10.

def perimetre(x):
    return x * 4

nbr_coté = 10
print(f"le périmetre d'un carré de coté {nbr_coté} est egal a {perimetre(nbr_coté)}")


# Exercice 4 : Ecrire une fonction aire qui prend deux paramètres : la longueur d'un rectangle et sa largeur, et qui renvoie l'aire du rectangle correpondant.
# Tester ensuite cette fonction avec deux instructions assert().


def perimetre(x, y):
    return x * 2 + y * 2

nbr_coté_x = 10
nbr_coté_y = 20
print(f"le périmetre d'un rectangle de coté {nbr_coté_x} x {nbr_coté_y} est egal a {perimetre(nbr_coté_x, nbr_coté_y)}")


assert(perimetre(nbr_coté_x, nbr_coté_y) == 60)

assert(perimetre(nbr_coté_x, nbr_coté_y) == 61)
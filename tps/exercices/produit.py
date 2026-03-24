#  Exercice 2 Produit des éléments d'un liste
# Ecrire une fonction produit qui prend en paramètre une liste d'entiers appelée liste et qui renvoie le produit des éléments de cette liste. 

def produit(liste):
    taillelist = len(liste)
    produit = 1
    for i in range(0, taillelist):
        
        produit = produit * liste[i]
    return produit 


print(produit([2,1,3,4]))

print(produit([8,2,4,2]))
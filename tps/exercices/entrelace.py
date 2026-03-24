# Exercice 3 Entrelacer deux listes
# Ecrire une fonction entrelace qui entrelace les deux listes liste1 et liste2 données en paramètre.
# Plusieurs méthodes sont envisageables. 

def entrelace(liste1, liste2):
    listeentrelace = []
    for a,b in zip(liste1,liste2):
        listeentrelace.append(a)
        listeentrelace.append(b)
    return listeentrelace


liste1 = [4,8,6,0,6,4]
liste2 = [5,1,9,3,7,3]
print(entrelace(liste1,liste2))
assert(entrelace(liste1,liste2) == [4,5,8,1,6,9,0,3,6,7,4,3])
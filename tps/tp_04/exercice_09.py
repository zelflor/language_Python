# Exercice 9 : Redéfinir la fonction min() avec deux paramètres pour qu'elle renvoie le maximum des deux paramètres.
# Effectuer ensuite un appel à la fonction min() avec deux et avec trois paramètres.

def min(param1, param2):
    return max(param1, param2)
    

print(f"{min(2, 8)}")
# print(f"{min(8, 3, 95)}")
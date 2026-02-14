# Exercice 5 : Ecrire une fonction rectangle() qui prend trois paramètres : le nombre de lignes, le nombre de colonnes et un caractère à afficher.
# Cette fonction devra afficher un rectangle . Par exemple l'appel rectangle(2,5,'A') devra afficher :
# AAAAA
# AAAAA
# Tester ensuite votre fonction avec divers appels.

def rectangle(x,y,letter):
    for i in range(x):
        print("")
        for n in range(y):
            print(f"{letter}", end="")
    
rectangle(2, 5, 'A')
    
rectangle(8, 4, 'B')
    
rectangle(1, 2, 'C')
    
rectangle(2, 1, 'A')
# Exercice 15 : Quel est le rôle du programme ci-dessous et comment s'appelle la méthode employée ici ? 

liste = list(range(2,100))
liste = [n for n in liste if n==2 or not(n%2 == 0)] # on supprime les nombres pairs sauf le premier
liste = [n for n in liste if n==3 or not(n%3 == 0)] 
liste = [n for n in liste if n==5 or not(n%5 == 0)]
liste = [n for n in liste if n==7 or not(n%7 == 0)]
print(liste)

# Le code si dessous permet de enchainer les conditions pour les chiffres a l'interieur plutot que d'utiliser une boucle for
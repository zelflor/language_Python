# Exercice 7 : Ecrire un programme qui demande à l'utilisateur de saisir son année de naissance, et qui lui répond en affichant son âge.
# Exemple d'affichage attendu : Tu as 15 ans. 

from datetime import *;

anneedeNaissance = input("donner l'année de Naissance : ")

now = datetime.now()

age = int(now.strftime("%Y")) - int(anneedeNaissance)

print(f"Tu as {age} ans")
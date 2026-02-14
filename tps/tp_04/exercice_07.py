# Exercice 7 : Ecrire une fonction bissextile(année) qui renvoie True si le paramètre correspond à une année bissextile et qui renvoie False sinon.
# Votre fonction ne doit utiliser ni des conditions imbriquées ni else ni des opérateurs booléens.
def bissextile(annee):
    if (annee % 400 == 0):
        return True
    if (annee % 4 == 0):
        if (annee % 100 != 0):
            return True
    return False


annee = int(input("Veuillez saisir une année : "))




if bissextile(annee):
    print(f"L'année {annee} est bissextile")
else:
    print(f"L'année {annee} n'est pas bissextile")
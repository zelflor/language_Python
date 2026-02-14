# Exercice 6 : Ecrire une fonction nbSecondes() qui prend trois paramètres : un nombre d'heures, un nombre de minutes et un nombre de secondes (par exemple (3,47,5) pour 3 heures 47 minutes 5 secondes) et qui renvoie le nombre total de secondes correspondant.
# Indiquer la valeur 0 comme valeur par défaut pour le nombre d'heures, le nombre de minutes et le nombres de secondes.
# Tester ensuite cette fonction avec zéro, un, deux et trois paramètres.

def nbSecondes(h = 0, m = 0, s = 0):
    m = m + h * 60
    s = s + m * 60

    return s

print(f"12h est egal à {nbSecondes(12, 0 , 0)} secondes")
print(f"24h est egal à {nbSecondes(12, 0 , 0)} secondes")

print(f"1 heure est egal à {nbSecondes(1, 0 , 0)} secondes")
print(f"60 minutes est egal à {nbSecondes(0, 60 , 0)} secondes")

print(f"12h02 et 40s est egal à {nbSecondes(12, 2 , 40)} secondes")
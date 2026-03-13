# Exercice 12 : Un hôtel comporte 19 chambres numérotées de 1 à 20, mais la chambre n°13 n'existe pas.
# Le programme ci-dessous affiche la liste de tous les numéros de chambres de l'hôtel.
# Le petit défaut (qui concerne seulement la lisibilité) de ce programme est que l'instruction print(i) est reléguée au 2ème niveau d'indentation alors qu'il s'agit de l'instruction qui est effectuée dans les cas ordinaires (et non dans le cas exceptionnel de la chambre n°13).
# Réécrire une version plus lisible de ce programme, dans laquelle l'instruction print(i) sera écrite au 1er niveau d'indentation. 

i = 0
while i < 20:
    i += 1
    if i == 13:
        continue

    print(i)
    
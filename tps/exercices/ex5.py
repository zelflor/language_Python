
#  Exercice 5 Listes définies en compréhension, filtrage d'une liste
# 1) Générer en compréhension la liste des carrés des entiers de 1 à 25 (liste1 à générer ci-dessous).
print([i**2 for i in range(1, 25) if i**2 < 26])

# 2) Générer en compréhension la liste des entiers de 0 à 100 qui ne sont pas divisibles par 7 (liste2 à générer ci-dessous). 

print([i for i in range(0, 100) if i % 7 != 0])
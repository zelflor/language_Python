# Exercice 2 : La population d'un village de 1000 habitants diminue chaque année de 1%.
# Ecrire un programme qui calcule le nombre d'années au bout duquel la population de ce village aura diminué de moitié. 


habitants = 1000
years = 0
while habitants >= 500:
    
    habitants = habitants * 0.99
    years += 1

print(years)
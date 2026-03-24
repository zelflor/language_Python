# Exercice 2 : Le programme ci-dessous affiche les niveaux de rouge, vert, bleu du pixel de coordonnées (200,100).
# Modifier ce programme pour qu'il affiche les niveaux de rouge, vert, bleu du coin supérieur gauche de l'image.

# Remarque : la fonction getpixel prend en argument un tuple (un couple) (x,y) de deux nombres entiers qui correspondent aux coordonnées d'un pixel de l'image.
from PIL import Image

image = Image.open('Perroquet.jpg')

rouge, vert, bleu = image.getpixel((0,0))   # on récupère les niveaux de rouge/vert/bleu du pixel de coordoonées (200,100)
print("Rouge :", rouge, "Vert :",vert, "Bleu : ", bleu)
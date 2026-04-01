# Exercice 6 :
# 1) Ecrire un programme qui éclaricit l'image en multipliant par 2 les niveaux de rouge/vert/bleu de chaque pixel.
# 2) Quels sont les défauts de cette méthode ?
# 3) Comment peut-on améliorer cet algorithme d'éclaircissement d'une image ? 

from PIL import Image
import math

def f(x):
    return x * 2   # Fonction à modifier

image = Image.open('Perroquet.jpg')
largeur, hauteur = image.size 
for x in range(largeur): 
    for y in range(hauteur):
        rouge, vert, bleu = image.getpixel((x,y))  
        nouveauRouge, nouveauVert, nouveauBleu = f(rouge), f(vert), f(bleu)
        image.putpixel( (x, y), (nouveauRouge, nouveauVert, nouveauBleu) )
image.show()
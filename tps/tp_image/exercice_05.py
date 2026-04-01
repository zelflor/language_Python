# Exercice 5 :
# 1) Compléter le deuxième programme ci-dessous pour qu'il affiche une version assombrie de l'image en divisant par 2 les niveaux de rouge/vert/bleu de chaque pixel.
# 2) Pour plus d'efficacité, utiliser une fonction 𝑓 qui à partir d'une intensité lumineuse de départ 𝑥 renvoie une intensité lumineuse plus faible 𝑓(𝑥). 
from PIL import Image

def f(x):
    return x // 2



image = Image.open('Perroquet.jpg')
largeur, hauteur = image.size 

for x in range(largeur): 
    for y in range(hauteur):
        rouge, vert, bleu = image.getpixel((x, y))  
        nouveauRouge = f(rouge)
        nouveauVert = f(vert)
        nouveauBleu = f(bleu)
        image.putpixel( (x, y), (nouveauRouge, nouveauVert, nouveauBleu) )
image.show()
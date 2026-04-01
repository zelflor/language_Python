# Exercice 8 : Ecrire un programme qui transforme une image en son négatif, c'est-à-dire qui transforme les pixels clairs en pixels sombres et inversement. 

from PIL import Image

image = Image.open('Perroquet.jpg')
largeur, hauteur = image.size 
for x in range(largeur): 
    for y in range(hauteur):
        rouge, vert, bleu = image.getpixel((x, y))  

        nouveauRouge = (255 - rouge)
        nouveauVert = (255 - vert)
        nouveauBleu = (255 - bleu)
        image.putpixel( (x, y), (nouveauRouge ,nouveauVert, nouveauBleu) )
image.show()
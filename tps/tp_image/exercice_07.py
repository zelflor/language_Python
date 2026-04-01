# Exercice 7 : Ecrire un programme qui transforme les couleurs de l'image en niveaux de gris, de façon à ce que l'image apparaisse en "noir et blanc".
# Indication : pour qu'un pixel apparaisse "gris", ses niveaux de rouge/vert/bleu doivent être identiques.
# Remarque : une autre transformation amusante consiste à intervertir les niveaux de rouge/vert/bleu. 


from PIL import Image

image = Image.open('Perroquet.jpg')
largeur, hauteur = image.size 
for x in range(largeur): 
    for y in range(hauteur):
        rouge, vert, bleu = image.getpixel((x, y))  
        moyennecouleur = (rouge + bleu + vert) // 3
        nouveauRouge = moyennecouleur
        nouveauVert = moyennecouleur
        nouveauBleu = moyennecouleur
        image.putpixel( (x, y), (nouveauRouge ,nouveauVert, nouveauBleu) )
image.show()
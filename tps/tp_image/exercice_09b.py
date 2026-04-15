# Exercice 9 b: Ecrire un programme transforme l'image en son reflet dans un miroir, en inversant la gauche et la droite. 

from PIL import Image

image = Image.open('Perroquet.jpg')
largeur, hauteur = image.size 
for x in range(largeur // 2): 
    for y in range(hauteur):
        rouge, vert, bleu = image.getpixel((x, y))  
        rouge2, vert2, bleu2 = image.getpixel((largeur - 1 - x, y))  

        image.putpixel( (x, y), (rouge2 ,vert2, bleu2) )
        image.putpixel( (largeur - 1 - x, y), (rouge ,vert, bleu) )
image.show()
# Exercice 9 : Ecrire un programme transforme l'image en son reflet dans un miroir, en inversant la gauche et la droite. 

from PIL import Image

image = Image.open('Perroquet.jpg')
image2 = Image.open('Perroquet.jpg')
largeur, hauteur = image.size 
for x in range(largeur): 
    for y in range(hauteur):
        rouge, vert, bleu = image.getpixel((x, y))  

        image2.putpixel( (-x, -y), (rouge ,vert, bleu) )
image2.show()
# Exercice 3 : Le programme ci-dessous fixe les niveaux de rouge/vert/bleu à 255 pour le pixel de coordonnées (200,100).
# 1) Quelle est la couleur du pixel ainsi modifié ? Le voyez-vous sur l'image ?
# 2) Modifier la couleur d'un autre pixel situé dans une zone claire de l'image et attribuer une couleur sombre à ce pixel.

# Remarque : la fonction putpixel prend en argument deux tuples : un couple (x,y) de deux nombres entiers qui correspondent aux coordonnées d'un pixel de l'image ; un triplet (r,v,b) qui correspond aux niveaux de rouge/vert/bleu de la nouvelle couleur que l'on souhaite attribuer au pixel de coordonnées (x,y).


image = Image.open('Perroquet.jpg')
image.putpixel( (200,100), (255,255,255) )


# On vois un pixel blanc

image.putpixel( (260,100), (0,0,0) )

image.show()
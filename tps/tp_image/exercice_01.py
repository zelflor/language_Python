from PIL import Image

image = Image.open('Perroquet.jpg')     # chargement de l'image
largeur, hauteur = image.size           # on récupère les dimensions de l'image
print("Largeur en pixels :", largeur, " Hauteur en pixels :", hauteur)
print(f"Nombre total de pixel : {largeur * hauteur}")
image.show()
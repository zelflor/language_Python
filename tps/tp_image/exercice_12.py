# Exercice 12 : Ecrire un programme qui floute la tête du perroquet. Pour flouter une image, 
# on remplace la couleur de chaque pixel par la moyenne des couleurs des pixels environnants.
#  Voici la signature de la fonction qui calcule la moyenne des couleurs des pixels environnants.


from PIL import Image

image = Image.open('Perroquet.jpg')
imagereturn = Image.open('Perroquet.jpg')
largeur, hauteur = image.size 

zone_head_start_x = 222
zone_head_start_y = 10
zone_head_end_x = 350
zone_head_end_y = 128

def moyenne(x, y, n):
    moyennerouge = 0
    moyennevert = 0
    moyennebleu = 0
    for indexx in range((x - n // 2), (x + n // 2), 1):
        for indexy in range((y - n // 2), (y + n // 2), 1):
            rouge, vert, bleu = image.getpixel((indexx, indexy))  
            moyennerouge += rouge
            moyennevert += vert
            moyennebleu += bleu
    
    moyennerouge = moyennerouge // (n * n)
    moyennevert = moyennevert // (n * n)
    moyennebleu = moyennebleu // (n * n)
    moyenne = [moyennerouge, moyennevert, moyennebleu]
    return moyenne



radius_blur = 15


for x in range(largeur): 
    for y in range(hauteur):
        rouge, vert, bleu = image.getpixel((x, y))  
        if ((x >= zone_head_start_x and y >= zone_head_start_y) and x <= zone_head_end_x and y <= zone_head_end_y):
            
            moyenne_pixel = moyenne(x,y, radius_blur)

            imagereturn.putpixel( (x, y), (moyenne_pixel[0] ,moyenne_pixel[1], moyenne_pixel[2]) )
        
        else:
            imagereturn.putpixel( (x, y), (rouge ,vert, bleu) )

imagereturn.show()



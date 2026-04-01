from PIL import Image

image = Image.open('vache.jpg')


def milka(image):
    """ Fonction qui permet de transformer l'image d'une vache en vache milka"""

    facteur_darkness = 0.8
    
    rouge_milka = 74
    bleu_milka = 57
    vert_milka = 132
    
    zone_vache_start_x = 63
    zone_vache_start_y = 57
    zone_vache_end_x = 675
    zone_vache_end_y = 277
    
    largeur, hauteur = image.size 
    for x in range(largeur): 
        for y in range(hauteur):
            rouge, vert, bleu = image.getpixel((x, y))  
            if (((rouge + bleu + vert) // 3) < 70):
                if ((x >= zone_vache_start_x and y >= zone_vache_start_y) and x <= zone_vache_end_x and y <= zone_vache_end_y):
                    image.putpixel( (x, y), ((rouge_milka + int(((rouge + bleu + vert) // 3) * facteur_darkness)) ,(bleu_milka + int(((rouge + bleu + vert) // 3) * facteur_darkness) ), (vert_milka + int(((rouge + bleu + vert) // 3) * facteur_darkness))) )
            else:
                image.putpixel( (x, y), (rouge ,vert, bleu) )

milka(image)
image.show()



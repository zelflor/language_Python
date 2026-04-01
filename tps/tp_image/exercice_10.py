from PIL import Image

sprite = Image.open('sprite.bmp')

image = Image.open('Perroquet.jpg')



largeur, hauteur = sprite.size 
for x in range(largeur): 
    for y in range(hauteur):                    
        rouge, vert, bleu = sprite.getpixel((x, y))  
        if (vert != 255 and rouge != 0 and bleu != 0):
            image.putpixel( (x, y), (rouge ,vert, bleu) )

image.show()
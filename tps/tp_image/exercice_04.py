image = Image.open('Perroquet.jpg')

largeur, hauteur = image.size

taillerect = 200

centerl= largeur / 2
centerh = hauteur / 2

for x in range(centerl - taillerect / 2,centerl + taillerect / 2):
    for y in range(100,200):
        image.putpixel((x,y),(0,0,0))
image.show()
# Exercice 11 : La fonction triangle() ci-dessous permer de dessiner un triangle dont la base est horizontale et dont les coordonnées du sommet sont (x,y).
# 1) En utilisant la fonction triangle(), créer une fonction sapin(x,y) qui dessine un sapin tel que celui dessiné ci-dessous.
# 2) Créer une fonction forêt(n) qui dessine une forêt de n sapins dont la position est choisie aléatoirement. 

from turtle import *
from random import *
wn = Screen()

wn.tracer(0)

def triangle(x,y,côté,couleur):
    speed(15)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    color('black',couleur)
    left(210)
    forward(côté)
    left(150)
    forward(côté*1.732)
    left(150)
    forward(côté) 
    left(210)
    end_fill()


def sapin(x):
        
    for i in range(30):
        triangle(x, (-15 * i) + 300, 70, 'brown')

    for y in range(14):
        triangle(x, (-25 * y) + 300, 125, 'green')    
        

def foret(n):
    for i in range(n):
        sapin(-300 + i * n * 15)
    
foret(10)

wn.update()

wn.mainloop()
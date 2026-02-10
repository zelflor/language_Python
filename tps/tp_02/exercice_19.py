# Exercice 19 : Dessiner le drapeau de la France avec Turtle.

from turtle import *   

speed(5)
begin_fill()

for i in range(2):
    begin_fill()
    color('blue', 'blue')
    forward(50)
    left(90)
    forward(100)
    left(90)
forward(50)
end_fill()
begin_fill()
for i in range(2):
    color('white', 'white')
    forward(50)
    left(90)
    forward(100)
    left(90)

forward(50)
end_fill()
begin_fill()
for i in range(2):
    color('red', 'red')
    forward(50)
    left(90)
    forward(100)
    left(90)

forward(50)
end_fill()



done()
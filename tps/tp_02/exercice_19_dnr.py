from turtle import *   

speed(15)


for i in range(1, 6):
    
    begin_fill()
    if (i == 1 or i == 5):
            color('LightSkyBlue', 'LightSkyBlue')
    elif(i == 2 or i == 4):
            color('pink', 'pink')
    else:
            color('white', 'white')

    for y in range(1, 5):
       
        if (y == 1 or y == 3):
            forward(500)
        else :
            forward(100)
        
        left(90)

    end_fill()

    left(180 + 90)

    forward(100)
    left(90)




done()
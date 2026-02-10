from turtle import *   

speed(5)


for i in range(1 , 2):
    
    color('blue')
    goto(0, 0)

    goto(-200, 0)

    goto(200, 0)
    goto(0, 0)
    goto(0, 100)
    goto(0, -100)
    
    for i in range(5):
        goto(0, 100)
        goto(i * 50, 00)
        goto(0, 100)
    for i in range(5):
        goto(0, -100)
        goto(i * 50, 00)
        goto(0, -100)
    goto(0, 0)
    for i in range(5):
        goto(0, -100)
        goto(-i * 50, 0)
        goto(0, -100)
    for i in range(5):
        goto(0, 100)
        goto(-i * 50, 0)
        goto(0, 100)
    done()

import p5

grille = [[0]*15 for i in range(10)] 


saisie = int(input("choisir ça config :"))


match saisie:
    case 1:
        grille[2][1] = 1
        grille[3][4] = 1
    case 2:
        grille[2][1] = 1
        grille[2][4] = 1
        grille[4][1] = 1
        grille[4][4] = 1
        grille[5][2] = 1
        grille[5][3] = 1
    case 3:
        taillecarre = 9
        for i in range(0, taillecarre):
            grille[0][i] = 1
        for i in range(0, taillecarre):
            grille[i][0] = 1
        for i in range(0, taillecarre):
            grille[taillecarre][i] = 1
        for i in range(0, taillecarre):
            grille[i][taillecarre] = 1
        grille[taillecarre][taillecarre] = 1

        for i in range(0, taillecarre):
            grille[i][i] = 1

def setup():
    largeur = 600
    hauteur = 400
    p5.createCanvas(largeur,hauteur)
    p5.background(0,0,255)  
    p5.noLoop()

def draw():   
    côté = 40
    p5.stroke(255,0,0)
    for i in range(10):
        for j in range(15):            
            if grille[i][j] == 0:                
                p5.fill(255,255,255)
            else:
                p5.fill(100,200,50)
            p5.rect(j*côté,i*côté,côté,côté)    

p5.run()
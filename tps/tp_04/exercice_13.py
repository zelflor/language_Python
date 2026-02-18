# Exercice 13 : Ecrire une fonction de votre choix, ainsi qu'une variable 
# globale compteur qui compte le nombre de fois où votre fonction a été appelée. 


def meow():
    global b
    print('meow')
    b += 1

b = 0 
meow()
meow()
meow()
print(b)
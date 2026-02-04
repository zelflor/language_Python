hauteur = int(input("Veuillez saisir la hauteur du triangle : "))
hauteur += 1

for i in range(hauteur):
    for y in range(i):
        print("*", end="")
        
    print("")
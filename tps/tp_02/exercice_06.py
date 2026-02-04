nbrligne = input("Entrez le nombre de ligne")
nbrcaractere = input("Entrez nombre de caractère")

nbrcaractere = int(nbrcaractere)

nbrligne = int(nbrligne)

for i in range(nbrligne):
    print("")
    for y in range(nbrcaractere):
        print("#", end="")
        
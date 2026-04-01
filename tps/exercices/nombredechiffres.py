nbr = int(input('Entrez un nombre :'))

nbrchiffres = 0

while (nbr) > 0:
        nbr = nbr // 10 ** nbrchiffres
    nbrchiffres += 1

print(nbrchiffres)
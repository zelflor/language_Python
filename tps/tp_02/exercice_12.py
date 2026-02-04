somme = 0
for i in range(5):
    nbrnote = int(input(f"Entrez la note {i + 1} : "))
    somme = somme + nbrnote

somme = somme / 5

print(somme)
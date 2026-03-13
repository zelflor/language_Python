# Exercice 12 : Ecrire un programme qui demande à l'utilisateur de saisir successivement deux mots écrits en minuscules (on évitera les lettres accentuées) puis qui les affiche l'un après l'autre dans l'ordre alphabétique.

mot1 = input("Entrez votre premier mot en minuscule sans accent : ")
mot2 = input("Entrez votre deuxieme mot en minuscule sans accent : ")

def isletter(mot1, letter):

    letter = chr(letter)
    taillemot = len(mot1)

    nbr_letter = 0

    i = 0
    while i < taillemot:
        if (mot1[i] == letter):
            nbr_letter += 1
        i += 1 
    if (nbr_letter > 0):
        return nbr_letter
    else:
        return False

for i in range(97, 123):
    
    if (isletter(mot1, i) != False):
        y = 0
        while(y < isletter(mot1, i)):
            print(chr(i), end="")
            y += 1
    if (isletter(mot2, i) != False):
        y = 0
        while(y < isletter(mot2, i)):
            print(chr(i), end="")
            y += 1
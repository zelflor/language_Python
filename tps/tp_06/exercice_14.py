# Exercice 14 : Ecrire une fonction transforme(mot) qui prend en paramètre un mot écrit avec des majuscules et/ou des minuscules, et qui renvoie ce mot avec la première lettre en majuscule et les autres lettres en minuscule. 

def transforme(mot):
    mot = mot.lower()
    # mottaille = len(mot)
    motfinal = mot[0].upper() + mot[1:].lower()
    return motfinal


print(transforme("fraise"))
print(transforme("FRAISE"))
print(transforme("fRAISE"))
print(transforme("Fraise"))
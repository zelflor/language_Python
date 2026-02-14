# Exercice 3 : Voici la table de vérité de l'opérateur booléen "OU exclusif", XOR en anglais (eXclusive OR):
        # 𝑐1
        #  	 𝑐2
        #  	 𝑐1
        #   xor  𝑐2
        
        # Vrai	Vrai	Faux
        # Vrai	Faux	Vrai
        # Faux	Vrai	Vrai
        # Faux	Faux	Faux
# Créer une fonction xor qui prend en paramètre deux booléens et qui renvoie la valeur True ou False selon les cas.
# Tester ensuite cette fonction dans chacun des quatre cas de la table de vérité.

def xor(c1, c2):
    if (c1):
        if c2:
            return False
        else:
            return True
    else:
        if c2:
            return True
        else:
            return False
        
cas1 = xor(True, True)
cas2 = xor(True, False)
cas3 = xor(False, True)
cas4 = xor(False, False)

print(f"{cas1} {cas2} {cas3} {cas4}")
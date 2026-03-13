def division(a,b):
    assert type(a) == type(1), "Le type du premier paramètre a doit être entier!"
    assert a>=0, "Le premier paramètre a doit être positif ou nul!"
    assert type(b) == type(1), "Le type du second paramètre b doit être entier!"
    assert b>0, "Le second paramètre b ne doit pas être nul et doit être positif!"    
    # code de la fonction division à compléter ici
    valeur = 0
    while a >= b:
        a = a - b
        valeur += 1
    
    return valeur


# print (division(19,3))
# print (division(18,3))
# print (division(0,5) )
# Quelques tests
assert division(19,3) == 6
assert division(18,3) == 6
assert division(0,5) == 0
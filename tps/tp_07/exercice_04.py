# Exercice 4 : Dans le programme précédent, ajoutez une ou plusieurs notes à la liste et recalculez la moyenne des notes.

notes = [12,17,15,14, 20, 15]
somme = 0
for i in range(len(notes)):
    somme = somme + notes[i]
moyenne = somme / len(notes)
print(moyenne)
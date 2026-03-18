# Exercice 11 : Ecrire ci-dessous un programme qui trace la courbe représentative de la fonction racine carrée sur l'intervalle [0;100].

import matplotlib.pyplot as plt

abscisses = []
ordonnées = []
for i in range(100):
    abscisses.append(i**2)
    ordonnées.append(i)



plt.plot(abscisses, ordonnées)
plt.title('Courbe de la fonction carré sur [0;100]')
plt.xlabel('x')
plt.ylabel('x²')
plt.show()
print(abscisses)
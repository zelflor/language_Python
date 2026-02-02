# Exercice 5 : Ecrire un programme qui permute les valeurs des variables 𝑎, 𝑏 et 𝑐.
# Dans l'exemple ci-dessous, après exécution du programme, 𝑎 devra être égal à 4, 𝑏 devra être égal à 8 et 𝑐 devra être égal à 7.
# Votre programme doit fonctionner quelles que soient les valeurs initiales données à 𝑎, 𝑏 et 𝑐. 

a = 5
b = 9
c = 15

d = a + b + c

a = d - a - c

b = c

c = d - (a + b)
 

print(a, b, c)
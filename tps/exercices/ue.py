import random

pays = ['Allemagne', 'Autriche', 'Belgique', 'Bulgarie', 'Chypre', 'Croatie', 'Danemark', 'Espagne', 'Estonie', 'Finlande',
        'France', 'Grèce', 'Hongrie', 'Irlande', 'Italie', 'Lettonie', 'Lituanie', 'Luxembourg', 'Malte', 'Pays-Bas', 
        'Pologne', 'Portugal', 'République tchèque', 'Roumanie', 'Slovaquie', 'Slovénie', 'Suède']
capitale = ['Berlin', 'Vienne', 'Bruxelles', 'Sofia', 'Nicosie', 'Zagreb', 'Copenhague', 'Madrid', 'Tallinn', 'Helsinki',
           'Paris', 'Athènes', 'Budapest', 'Dublin', 'Rome', 'Riga', 'Vilnius', 'Luxembourg', 'La Valette', 'Amsterdam',
           'Varsovie', 'Lisbonne', 'Prague', 'Bucarest', 'Bratislava', 'Ljubljana', 'Stockholm']
population = [83.16, 8.98, 11.75, 6.45, 0.90, 3.85, 5.93, 47.43, 1.37, 5.56,
             68.4, 10.71, 9.60, 5.27, 58.98, 1.88, 2.9, 0.66, 0.54, 17.81,
             36.7, 10.5, 10.7, 19.06, 5.43, 2.11, 10.45]

# Exercice 1 Les pays de l'Union Européenne
# On donne ci-dessous la liste des pays de l'Union européenne (UE), ainsi que la liste des capitales correspondantes et la liste des nombres d'habitants (en millions d'habitants).
# Répondre aux questions suivantes en écrivant un petit programme en Python.


print(f"1) Combien y a-t-il de pays dans l'UE ?")
print(f"{len(pays)}")

print(f"2) Quel est le nombre total d'habitants de l'UE ?")
nbrHabitants = 0
for i in range(len(population)):
    nbrHabitants += population[i]
print(f"{round(nbrHabitants, 2)}")


print(f"3) Quel est le pays le plus peuplé de l'UE ? ")

indexPlusHabitants = 0
for i in range(len(population)):
    if population[indexPlusHabitants] < population[i]:
        indexPlusHabitants = i
print(pays[indexPlusHabitants])


print(f"4) Quel est le pays le moins peuplé de l'UE ? ")

indexLessHabitants = 0
for i in range(len(population)):
    if population[indexLessHabitants] > population[i]:
        indexLessHabitants = i
print(pays[indexLessHabitants])


print(f"5) Ecrire un programme qui affiche un pays de l'UE au hasard, ainsi que sa capitale et son nombre d'habitants.")
randomIndexPays = random.randint(0, len(pays))

print(f"Information a propos de : {pays[randomIndexPays]}, ça capital est {capitale[randomIndexPays]} et ce pays contient {population[randomIndexPays]} Million(s) d'habitants")


print(f"6) Ecrire un programme qui demande à l'utilisateur de saisir le nom d'un pays de l'UE et qui affiche la capitale de ce pays. ")

saisiepays = input("Entrez un nom de pays : ")
if saisiepays in pays:
    for i in range(len(pays)):
        if (saisiepays == pays[i]):
            print(capitale[i])
            break
# Exercice 9 : Ecrire un programme qui :

#     Demande à l'utilisateur sa taille en cm
#     Crée une variable booléenne appelée "grand" dont la valeur dépend de la taille saisie
#     Affiche un message différent selon que l'utilisateur est grand ou pas
#     Par exemple : "Vous avez le droit (ou pas le droit) de monter dans ce manège."

taille_cm = int(input("Entrez votre taille en cm : "))
grand = False

if (taille_cm > 130):
    grand = True

if grand:
    print("ous avez le droit de monter dans ce manège.")
else:
    print("ous avez pas le droit de monter dans ce manège")
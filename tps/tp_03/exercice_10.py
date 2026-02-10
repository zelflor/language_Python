#  Ecrire un programme qui demande à l'utilisateur sa moyenne du bac et qui lui indique sa mention.

moyenne_bac = int(input("Entrer votre moyenne du bac : "))
mention = ""


if (moyenne_bac < 8):
    mention = "Recalé"
elif (moyenne_bac < 10):
    mention = "Rattrapage"
elif (moyenne_bac < 12):
    mention = "Sans mention"
elif (moyenne_bac < 14):
    mention = "mention Assez bien"
elif (moyenne_bac < 16):
    mention = "mention Bien"
elif (moyenne_bac < 18):
    mention = "mention Très bien"
elif (moyenne_bac < 21):
    mention = "mention Félicitations"
else :
    mention = "??????"

print(f"Avec votre moyenne de {moyenne_bac} vous avez eu {mention}")
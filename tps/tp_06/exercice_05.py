# Exercice 5 : Ecrire un programme qui affiche la dernière lettre d'un mot saisi par l'utilisateur. 

saisie = input("Entrez un mot : ")

taillesaisie = len(saisie)

print(f"La dernière lettre est {saisie[taillesaisie - 1]}")
print(f"La dernière lettre est {saisie[-1]}")
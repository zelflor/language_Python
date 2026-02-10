# Exercice 4 : Ecrire un programme qui demande à l'utilisateur de saisir le mot de passe qui permet de se connecter au serveur de la NASA, et qui lui indique si l'accès est autorisé ou pas.
# Le mot de passe est "azerty". 

pwd = "azerty"
saisie_pwd = input("Entrez le Password de l'ordinateur ultra sonique de la NASA : ")

if (pwd == saisie_pwd):
    print("Vous etes connecter, ne lancer pas de fusée stp")
else :
    print("Mot de passe incorrect")
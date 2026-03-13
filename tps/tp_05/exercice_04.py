# Exercice 4 : Ecrire un programme qui attend que l'utilisateur ait saisi le bon mot de passe avant de lui donner l'accès.
# Le mot de passe est "PIZZA". 

password = "PIZZA"
enter_password = ""


while enter_password != password :
    enter_password = input("Entrez le mot de passe")
    
print("Bienvenue dans l'entre de la pizza")
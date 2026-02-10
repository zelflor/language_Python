# Exercice 13 : Reprendre le problème des années bissextiles (exercice 11) en utilisant des opérateurs booléens à la place des conditions imbriquées.
# Une année est bissextile si elle est multiple de 4 mais pas multiple de 100, ou si elle est multiple de 400.
# Tester ensuite votre programme avec les années 2021, 2020, 1900 et 2000. 

# année = int(input("Veuillez saisir une année : "))

# bissectile = False

# if (année % 4 == 0):
#     if (année % 100 == 0):
#         if (année % 400 == 0):
#             bissectile = True
#     else:
#         bissectile = True

# if (bissectile):
#     print(f"l'année {année} est bissectile")
# else:
#     print(f"l'année {année} n'est pas bissectile")
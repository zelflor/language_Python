# Exercice 13 : Comme chaque année, lors de la rentrée universitaire, de nombreux étudiants viennent s’inscrire à la bibliothèque et une longue file d’attente se forme. Afin d’essayer d'accélérer les choses, les fiches d’inscription de tous les étudiants ont déjà été préparées et ils n’ont plus qu’à les récupérer.

# Trois personnes sont en charge de distribuer les fiches : la première s’occupe des étudiants dont le nom commence par une lettre comprise entre A et F (inclus), la seconde personne des étudiants dont le nom commence par une lettre comprise entre G et P (inclus) et la troisième du reste des étudiants.

# Quand un nouvel étudiant arrive, il donne son nom et il faut lui indiquer quelle personne il doit aller voir. Les noms des étudiants commencent par une lettre majuscule.

# Ecrire une fonction personne(étudiant) qui renvoie le numéro (1, 2 ou 3) de la personne que l'étudiant doit aller voir.
# Ajouter ensuite plusieurs instructions assert pour tester chacun des cas.
# Source : France IOI


def personne(etudiant):
    if (etudiant[0] > chr(64) and etudiant[0] < chr(71)):
        return 1
    elif(etudiant[0] > chr(70) and etudiant[0] <= chr(80)):
        return 2
    else :
        return 3
    
assert(personne("Queiroz") == 3)
assert(personne("Florian") == 1)
assert(personne("Paul") == 2)
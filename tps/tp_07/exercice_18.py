# Exercice 18 : Dans le programme ci-dessous, la liste nbCas contient le nombre de nouveaux cas de Covid-19 relevés chaque jour en France du 1er janvier 2020 au 2 avril 2021. Cette liste est représentée graphiquement en faisant appel à la bibliothèque matplotlib. On observe que les valeurs sont irrégulières avec des "creux" tous les sept jours dûs aux week end.
# Afin de mieux voir les tendances et de supprimer cet effet "week end", on lisse la courbe en utilisant une moyenne mobile à 7 jours. Ceci consiste à remplacer chaque valeur par la moyenne des valeurs des 7 jours précédents.

# Dans le programme, les 6 premières valeurs de la liste moyenneMobile7jours ont été initialisées à 15 000.
# Compléter cette liste afin qu'elle contienne les moyennes mobiles à 7 jours correspondant à chaque journée.

import matplotlib.pyplot as plt

#nombre de nouveaux cas quotidiens de Covid-19 en France du 1er janvier 2021 au 10 mai 2021
nbCas = [19348,3466,12489,4022,20489,25379,21703,19814,20177,15944,3582,19752,23852,21228,21271,
        21406,16642,3736,23608,26784,22848,23292,23924,18436,4240,22086,26916,23770,22858,24392,
        19235,4347,23337,26362,23448,22139,20586,19715,4317,18870,25387,21063,20701,21231,16546,
        4376,19590,25018,22501,24116,22371,22046,4646,20064,31519,25403,25207,23996,19952,4703,
        22857,26788,25279,23507,23306,21825,5327,23302,30303,27166,25229,29759,26343,6471,29975,
        38501,34998,35088,35327,30581,15792,14678,65373,45641,41869,42619,37014,9094,30702,59038,
        50659,46677,13917,66794,10793,8045,12951,84999,41243,43284,34895,8536,39113,43505,38045,
        36442,35861,29344,6696,43098,34968,34318,32340,32633,24465,5952,30317,31539,26538,24299,
        25670,9888,3760,24371,26000,21712,19124,20745,9128,3292]
abscisses = list(range(len(nbCas)))
moyenneMobile7jours = [15000] * 6

plt.plot(abscisses, nbCas)
plt.plot(moyenneMobile7jours)
plt.title('Nombre de nouveaux cas quoditiens de Covid-19 en France depuis le 1er janvier 2021')
plt.xlabel('numéro du jour')
plt.ylabel('nombre de cas')
plt.show()
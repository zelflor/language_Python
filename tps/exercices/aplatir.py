tableau = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

aplati = []

for i in range(0 , len(tableau)):
    for y in range(0, len(tableau[1])):
        aplati.append(tableau[i][y])

print(aplati)


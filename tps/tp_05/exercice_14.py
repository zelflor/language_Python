somme = 0
for i in range(10):    
    if i == 5:
        continue
    if i == 8:
        break
    somme = somme + i
print(somme)
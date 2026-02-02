# Exercice 6 : Exécutez l'algorithme suivant qui a été écrit pour échanger le contenu des variables a et b ci-dessous. Vous devez constater qu'il ne fonctionne pas. Proposez une modification en utilisant une variable c supplémentaire. 

a = 5
b = 7

print(a)
print(b)

c = a + b

a = c - a

b = c - b

print(a)
print(b)
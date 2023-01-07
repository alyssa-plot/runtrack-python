#Écrire un programme qui compte le nombre de multiples de 3 présents dans la liste
#L = [8, 24,48,2,16]

L = [8,24,48,2,16]
resultat = 0
for nombre in L:
        if nombre % 3 == 0:
            resultat += 1
print(resultat)

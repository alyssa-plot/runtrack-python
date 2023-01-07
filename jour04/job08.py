#Écrire un programme qui calcule la somme de toutes les valeurs paires de la liste
#L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
somme = 0
for nombres in L:
    if nombres % 2 == 0:
        somme += nombres

print(somme)
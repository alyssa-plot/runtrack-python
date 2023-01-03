a="Bonjour le monde"
letter="e"
i=0

while i<len(a):
    if a[i] == letter:
        print("e est contenu dans la chaine au caractère", i+1)
    else:
        print('la lettre e est absente de la chaine de caractère')
    i=i+1
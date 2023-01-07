#Écrire une fonction qui contient une liste nommée “fruits” qui contient les strings
#“pomme”, “cerise”, “orange”. Cette fonction doit à son appel ajouter à la liste “fruits” une
#String “Melon” à la fin de cette liste.

def food():
    fruits = ["pomme", "cerise", "orange"]
    fruits.append("Melon")
    return(fruits)

fruits = food()

print(fruits)
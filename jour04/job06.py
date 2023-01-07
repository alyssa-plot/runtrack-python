def food():
    fruits = ["pomme", "cerise", "orange",'melon']
    swap = fruits[len(fruits) -1]
    fruits[len(fruits) -1]= fruits[0]
    fruits[0]= swap
    return(fruits)

fruits = food()
print(fruits)
n = int(input("entrez le nombre de lignes: "))
alpha = "abcdefghijklmnopqrstuvwxyz"
i = 0
j = 0
index = 0

while i <= n:
    while j <= i:
        if index == 26:
            index = 0
        print(alpha[index],end='')
        j+=1
        index+=1
    j=0
    i+=1
    print('')
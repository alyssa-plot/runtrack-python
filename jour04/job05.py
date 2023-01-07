L = [1, 2, 3, 4, 5]

print(L[1])

def remplace(j, i):
    j[i] = j[i-1] + j[i+1]
    
remplace(L, 3)
print(L[-1])
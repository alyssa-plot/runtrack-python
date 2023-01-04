def calcule(num1, signe, num2):

    if signe == "+":
        somme = num1 + num2
    elif signe == "-":
        somme = num1 - num2
    elif signe == "*":
        somme = num1 * num2
    elif signe == "/":
        somme = num1 / num2
    elif signe == "%":
        somme = num1 % num2
    return(somme)
        
print(calcule(7,"+",7))
print(calcule(7,"-",7))
print(calcule(7,"*",7))
print(calcule(7,"/",7))
print(calcule(7,"%",7))
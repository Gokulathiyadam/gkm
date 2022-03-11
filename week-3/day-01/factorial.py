c = int(input(print("enter a number :")))
def calculateFactorial(f):
    fac = 1
    i=1
    while i <= f:
        fac*=i
        i+=1
    return fac


factorial = calculateFactorial(c)
print(factorial)

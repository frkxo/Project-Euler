from math import factorial

myList = list(str(factorial(100)))
myList = [int(x) for x in myList]
factorialSum = sum(myList)
print(factorialSum)

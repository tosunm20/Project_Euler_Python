def factorial(x):
    myresult = 1
    for i in range(1,x+1):
        myresult *= i
    return myresult

mynumber = factorial(100)
mynumber = str(mynumber)
mynumber.split()
mysum = 0
for rakam in mynumber:
    mysum += int(rakam)
print(mysum)

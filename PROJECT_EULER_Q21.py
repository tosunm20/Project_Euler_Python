def sumOfFactors(number):
    mySum = 0
    for i in range(1,(number // 2 + 1)):
        if number % i == 0:
            mySum += i
    return mySum

mySum2 = 0
for i in range(1,10001):
    x = sumOfFactors(i)
    if sumOfFactors(x) == i and i != x :
        mySum2 += x + i
mySum2 = mySum2 / 2
print(int(mySum2)) 
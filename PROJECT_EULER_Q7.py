from ast import Return
import math

def check_prime(number):
    isPrime = True
    if number == 2:
        return True
    else:
        for i in range(2,int(math.sqrt(number) + 1)):
            if number % i == 0:
                isPrime = False
        return isPrime

primeNumber = 2
count = 0

while True:
    if check_prime(primeNumber):
        count += 1
    if count == 10001:
        print(primeNumber)
        break
    primeNumber += 1

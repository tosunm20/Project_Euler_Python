import math

def prime_check(num):
    isPrime = True

    for i in range(2,int(math.sqrt(num))):
        if num % i == 0:
            isPrime = False
            continue
    
    return isPrime
mynumber = 600851475143
maxprime = 2

for i in range(2, int(math.sqrt(mynumber))):
    if mynumber % i == 0 and prime_check(i):
        maxprime = i

print(maxprime)
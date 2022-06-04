import math

def check_prime(number):
    isPrime = True

    if number == 2: return True

    else:
        for i in range(2,int(math.sqrt(number)+1)):
            if number % i == 0:
                isPrime = False
                break
        return isPrime

maxnum = 2000001
myresult = 0
for i in range(2,maxnum):
    if  check_prime(i):
        myresult += i
    else: continue    
print(myresult)
import math
def bolen(number):
    sayac = 1
    for i in range(2,int(math.sqrt(number)+1)):
        if number % i == 0:
            sayac += 1
        else:
            continue
    sayac *= 2
    return sayac

n = 1
while True:
    number = (n*(n+1))/2
    x = bolen(number)
    if x > 500:
        print(int(number))
        break
    n += 1

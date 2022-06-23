def myfactorial(number):
    fact = 1
    for i in range(1,number+1):
        fact *= i
    return fact

myresult = myfactorial(40) / (myfactorial(20) * myfactorial(20))
print(myresult)
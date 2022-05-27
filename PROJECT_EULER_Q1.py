mySum=0
for k in range(1,1000):
    if (k%3==0 or k%5==0):
        mySum=mySum+k
print(mySum)
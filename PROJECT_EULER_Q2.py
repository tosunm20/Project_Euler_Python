fibonacci = list()
fibonacci.append(1)
fibonacci.append(2)
index=2
while True:
    if (fibonacci[index-2]+fibonacci[index-1])<4000000:
        fibonacci.append(fibonacci[index-2]+fibonacci[index-1])
        index+=1
    else:
        break
mySum=0
for i in fibonacci:
     if i % 2 == 0:
         mySum+=i

print(mySum)
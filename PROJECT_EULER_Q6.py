squaredsum = 0
sumofsquares = 0
for i in range(1,101):
    squaredsum += i**2  # (1**2+2**2+...+100**2)
    sumofsquares += i  # (1+2+...+100)

squaresum = sumofsquares**2  # (1+2+...+100)**2
myresult = abs(squaresum - squaredsum)
print('My result is: ',myresult)

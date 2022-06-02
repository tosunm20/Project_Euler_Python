import math

bool1= False
for a in range(1,1000):
    
    for b in range(1,1000 - a):
        c = math.sqrt(a**2 + b**2)
        
        if (a + b + c) == 1000:
            print(a*b*c)
            bool1 = True
            break
    if bool1: # ** To prevent printing the result twice,...
              # ...you should also exit the outside loop. ** 
        break

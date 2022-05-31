def check_palindrom(x):
    if int(str(x)[::]) == int(str(x)[::-1]):
        return True
    else:
        return False

palinumber = 0
for i in range(100,1000):
    for j in range(100,1000):
        k = i*j
        if check_palindrom(k) and (k > palinumber):
            palinumber = k

print(palinumber)
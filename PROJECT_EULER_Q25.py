a1 = 1
a2 = 1

sayac = 2
while True:
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    if len(str(a3)) == 1000:
        print(sayac + 1)
        break
    else:
        sayac += 1
        continue

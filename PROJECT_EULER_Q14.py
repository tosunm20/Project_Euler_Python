onceki_sayilar = dict()

def collatz_sequence(number, onceki_sayılar):
    mynumber = number
    sayac = 1
    
    while number != 1:
        if number in onceki_sayilar:
            sayac += onceki_sayilar[number] - 1
            break
        if number % 2 == 0:
            number = number // 2
            sayac += 1
        else:
            number = 3*number + 1
            sayac += 1
    onceki_sayilar[mynumber] = sayac
    return sayac

sayi = 1
mycount = 1

for i in range(1,1000001):
    count_ = collatz_sequence(i, onceki_sayilar)
    if  count_ > mycount:
        mycount = count_
        sayi = i

print(mycount)
print(sayi)
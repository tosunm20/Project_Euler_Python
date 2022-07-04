import string

with open("p022_names.txt", "r") as f:
    names = f.read()

sozluk = dict()
alfabe = string.ascii_uppercase

i = 1
for harf in alfabe:
    sozluk[harf] = i
    i += 1

names = names.split(",")
list.sort(names)

index = 1
mysum = 0
for name in names:
    harfMysum = 0
    name = name[1:len(name)-1]
    for harf in name:
        harfMysum += sozluk[harf]
    
    mysum += harfMysum * index
    index += 1

print(mysum)
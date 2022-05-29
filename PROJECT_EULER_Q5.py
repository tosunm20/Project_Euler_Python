def divis1to20(x):
    for k in range(1,21):
        if x % k != 0:
            return False
    return True

num = 1
while True:
    if divis1to20(num):
        break
    num += 1

print(num)
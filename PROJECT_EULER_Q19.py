from datetime import date

sundaycounter = 0

for year in range(1901, 2001):
    for month in range(1,13):
        if date(year, month, 1).weekday() == 6:
            # last day,so 6
            sundaycounter += 1
print(sundaycounter)

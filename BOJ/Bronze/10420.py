year, month, day = 2014, 4, 1
leap_year = [i for i in range(2014, 2045) if i % 4 == 0 and i % 100 != 0 or i % 400 == 0]

n = int(input())

for _ in range(n):
    if month == 2:
        if day == 28 and year in leap_year:
            day = 29
        elif day == 28 and year not in leap_year or day == 29 and year in leap_year:
            day = 1
            month += 1
        else:
            day += 1
    elif month in [1, 3, 5, 7, 8, 10] and day == 31:
        day = 1
        month += 1
    elif month in [4, 6, 9, 11] and day == 30:
        day = 1
        month += 1
    elif month == 12 and day == 31:
        day = 1
        month = 1
        year += 1
    else:
        day += 1

print(f"{year}-{month:02d}-{day:02d}")
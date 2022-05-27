months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while 1:
    day, month, year = map(int, input().split())
    if day == month == year == 0:
        break
    res = sum(months[:month]) + day
    if month > 2 and year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        res += 1
    print(res)
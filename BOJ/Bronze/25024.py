month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for _ in range(int(input())):
    r1, r2 = "No", "No"
    x, y = map(int, input().split())
    if 0 <= x < 24 and 0 <= y < 60:
        r1 = "Yes"
    if 0 < x <= 12 and 0 < y <= month[x]:
        r2 = "Yes"
    print(r1, r2)


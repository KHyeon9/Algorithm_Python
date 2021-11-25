from math import floor, ceil
for _ in range(int(input())):
    y, m, d = map(int, input().split())
    n = 196471
    n2 = 0

    for i in range(1, y):
        if i % 3 == 0:
            n2 += 200
        else:
            n2 += 195

    if y % 3 == 0:
        n2 += 20 * (m - 1) + d

    else:
        n2 += ceil((m - 1) / 2) * 20 + floor((m - 1) / 2) * 19 + d
    print(n - n2)

from math import sqrt

while True:
    res = 100000
    d, e = map(int, input().split())

    if d == e == 0:
        break

    for i in range(d):
        now_price = abs(sqrt(i ** 2 + (d - i) ** 2) - e)
        res = min(res, now_price)

    print(f"{res:.4f}")
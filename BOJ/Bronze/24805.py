a, b, h = map(int, input().split())
now_h, res = 0, 0

while True:
    now_h += a
    res += 1

    if now_h >= h:
        print(res)
        break

    now_h -= b
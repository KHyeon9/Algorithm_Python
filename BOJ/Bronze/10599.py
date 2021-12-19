while 1:
    x1, x2, y1, y2 = list(map(int, input().split()))

    if x1 == x2 == y1 == y2 == 0:
        break

    else:
        r1 = abs(x1 - y2)
        r2 = abs(x2 - y1)

        print(min(r1, r2), max(r1, r2))
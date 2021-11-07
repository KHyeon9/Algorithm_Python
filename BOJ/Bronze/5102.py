while 1:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    else:
        r1 = max((a - b) // 2 - (a - b) % 2, 0)
        if (a - b) % 2 != 0 and (a - b) % 3 == 0:
            r2 = 1
        else:
            r2 = 0
        print(r1, r2)
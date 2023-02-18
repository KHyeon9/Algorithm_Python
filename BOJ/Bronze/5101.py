while 1:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    if (c - a) % b == 0 and (c - a) // b + 1 > 0:
        print((c - a) // b + 1)
    else:
        print('X')
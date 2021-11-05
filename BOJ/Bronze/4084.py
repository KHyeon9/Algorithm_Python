while 1:
    a, b, c, d = map(int, input().split())
    r = 0
    if a == b == c == d == 0:
        break
    while 1:
        if a == b == c == d:
            print(r)
            break
        a, b, c, d = abs(a - b), abs(b - c), abs(c - d), abs(d - a)
        r += 1
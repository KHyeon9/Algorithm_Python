while 1:
    a, b = list(input().split())
    r = int(b)
    if a == '#' and b == '0':
        break
    while 1:
        c, d = list(input().split())
        if c == 'X' and d == '0':
            break
        if c == 'B' and r + int(d) <= 68:
            r += int(d)
        if c == 'C' and r - int(d) >= 0:
            r -= int(d)
    print(a, r)
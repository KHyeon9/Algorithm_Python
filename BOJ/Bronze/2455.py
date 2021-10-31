p = 0
r = 0

while 1:
    m, n = map(int, input().split())
    if n != 0:
        p = p + n - m
        if r < p:
            r = p
    else:
        print(r)
        break

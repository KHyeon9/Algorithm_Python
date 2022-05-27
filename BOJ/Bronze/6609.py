while 1:
    try:
        m, p, l, e, r, s, n = map(int, input().split())

        for _ in range(n):
            temp = m
            m = p // s
            p = l // r
            l = temp * e
        print(m)
    except EOFError:
        break
while 1:
    try:
        n, m, b = map(float, input().split())
        res = 0
        while n < b:
            res += 1
            n += n * (m / 100)
        print(res)
    except EOFError:
        break
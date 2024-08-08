for _ in range(int(input())):
    res, now = 0, 0
    for _ in range(int(input())):
        p1, p2 = map(int, input().split())
        now = now - p1 + p2
        res = max(res, now)
    print(res)




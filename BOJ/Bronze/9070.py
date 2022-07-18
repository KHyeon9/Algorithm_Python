for _ in range(int(input())):
    g_w = [list(map(int, input().split())) for _ in range(int(input()))]
    start = 100001
    res = 0
    for i in range(len(g_w)):
        g, w = g_w[i]

        if start > w / g:
            start = w / g
            res = w
        elif start == w / g:
            res = min(res, w)
    print(res)
for _ in range(int(input())):
    l, r, n, m = map(int, input().split())
    gap = abs(n - m)
    if gap == 0:
        res = "G"
    elif l >= gap > r:
        res = "L"
    elif r >= gap > l:
        res = "R"
    else:
        res = "E"

    print(res)

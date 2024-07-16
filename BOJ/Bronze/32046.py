while True:
    n = int(input())

    if n == 0:
        break
    res = 0
    snacks = list(map(int, input().split()))

    for p in snacks:
        if res + p <= 300:
            res += p

    print(res)
for _ in range(int(input())):
    n, a, d = map(int, input().split())

    res = [a]

    for i in range(n - 1):
        res.append(res[-1] + d)

    print(sum(res))
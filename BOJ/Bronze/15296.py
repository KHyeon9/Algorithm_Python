for _ in range(int(input())):
    arr = []
    k, b, n = map(int, input().split())

    while n:
        arr.append(n % b)
        n //= b

    res = 0

    for a in arr:
        res += a ** 2

    print(k, res)
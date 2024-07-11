while True:
    n, m = map(int, input().split())

    if n == m == 0:
        break

    price = list(map(int, input().split()))
    res = -1
    for i in range(n - 1):
        for j in range(i + 1, n):
            sum_price = price[i] + price[j]
            if sum_price <= m:
                res = max(res, sum_price)
    print(res if res != -1 else "NONE")
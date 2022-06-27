k, n = map(int, input().split())
if n == 1:
    print(-1)
else:
    r = k * n // (n - 1)
    print(r if k * n % (n - 1) == 0 else r + 1)
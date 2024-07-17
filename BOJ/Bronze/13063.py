while True:
    n, m, k = map(int, input().split())

    if n == m == k == 0:
        break

    other = n - m - k
    half = n // 2 + 1
    if half - m > other:
        print(-1)
    else:
        print(max(half - m, 0))
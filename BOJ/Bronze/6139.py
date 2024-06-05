from math import ceil

n, k = map(int, input().split())

for _ in range(k):
    s, t, r = map(int, input().split())
    read = s * t
    res, cnt = 0, 0

    while True:
        if n - cnt <= read:
            res += ceil((n - cnt) / s)
            break

        cnt += read
        res += t + r

    print(res)
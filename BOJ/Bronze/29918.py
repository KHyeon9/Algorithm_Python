n0, m0 = map(int, input().split())
res = 0

for _ in range(5):
    n, m = map(int, input().split())
    res = max(res, (n - n0) + 10 * (m - m0) + 1)

print(res)
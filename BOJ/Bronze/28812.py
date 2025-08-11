n, c = map(int, input().split())
res = 1e9

for _ in range(n):
    p, d, v = map(int, input().split())
    res = min(res, p + d + v * c)

print(res)

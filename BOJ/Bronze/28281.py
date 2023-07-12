n, x = map(int, input().split())
socks = list(map(int, input().split()))
res = []

for i in range(n - 1):
    cost = socks[i] * x + socks[i + 1] * x
    res.append(cost)

print(min(res))
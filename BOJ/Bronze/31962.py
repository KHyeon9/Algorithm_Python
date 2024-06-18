res = []

n, x = map(int, input().split())

for _ in range(n):
    s, t = map(int, input().split())

    if s + t <= x:
        res.append(s)

print(sorted(res)[-1] if len(res) > 0 else -1)
res = []

for _ in range(5):
    n = int(input())
    if n in res:
        res.remove(n)
        continue
    res.append(n)

print(*res)
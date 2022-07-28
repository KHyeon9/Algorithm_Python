n, m = map(int, input().split())
max_l = min(n, m)
rac = [input() for _ in range(n)]
res = 0
for x in range(n):
    for y in range(m):
        for i in range(max_l):
            if (x + i < n and y + i < m) and rac[x][y] == rac[x][y + i] == rac[x + i][y] == rac[x + i][y + i]:
                res = max(res, (i + 1) ** 2)
print(res)



n, l = map(int, input().split())
res = []
total = -1
for i in range(l, 101):
    total = n - (i * (i - 1) / 2)
    if total % i == 0 and total >= 0:
        total = int(total / i)
        for j in range(i):
            res.append(total + j)
        print(*res)
        break
else:
    print(-1)

d = [0] + list(map(int, input().split()))
for i in range(1, 5):
    d[i] = d[i] + d[i - 1]

for i in range(5):
    res = []
    for j in range(5):
        res.append(abs(d[i] - d[j]))
    print(*res)



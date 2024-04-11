wm = sorted(list(map(int, input().split())))
res = 1e9

for i in range(4):
    for j in range(4):
        if i == j:
            continue
        temp1 = wm[i] + wm[j]
        diff = abs(sum(wm) - (temp1 * 2))
        res = min(res, diff)
    diff = abs(sum(wm) - (wm[i] * 2))
    res = min(res, diff)

print(res)



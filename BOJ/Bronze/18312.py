n, k = map(int, input().split())
k = str(k)
cnt = 0
for h in range(n + 1):
    h = str(h)
    if int(h) < 10:
        h = '0' + h
    for m in range(60):
        m = str(m)
        if int(m) < 10:
            m = '0' + m
        for s in range(60):
            s = str(s)
            if int(s) < 10:
                s = '0' + s
            if k in h + m + s:
                cnt += 1

print(cnt)
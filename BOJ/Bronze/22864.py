a, b, c, m = map(int, input().split())
time, work, cnt = 0, 0, 0
while time < 24:
    time += 1
    if cnt + a <= m:
        work += b
        cnt += a
    else:
        if cnt - c >= 0:
            cnt -= c
        else:
            cnt = 0
print(work)
x, y, p1, p2 = map(int, input().split())
cnt = 0
while cnt < max(p1, p2):
    if p1 < p2:
        p1 += x
    elif p1 > p2:
        p2 += y
    elif p1 == p2:
        print(p1)
        break
    if cnt > 1000:
        print(-1)
        break
    cnt += 1

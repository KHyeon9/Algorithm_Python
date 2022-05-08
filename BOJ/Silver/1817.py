N, M = map(int, input().split())
if N == 0:
    print(0)
else:
    weight = list(map(int, input().split()))
    cnt, m = 1, 0
    for w in weight:
        m += w
        if m > M:
            cnt += 1
            m = w

    print(cnt)

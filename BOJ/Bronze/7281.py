res, last_time = 0, 0

for _ in range(int(input())):
    t, m = map(int, input().split())

    if m == 1:
        res = max(res, t - last_time)
        last_time = t

print(res)
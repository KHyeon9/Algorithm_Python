n, f = map(int, input().split())
now_time, res = 1e9, 0

for i in range(n):
    x, v = map(int, input().split())
    time = (f - x) / v
    if now_time > time:
        now_time = time
        res = i + 1

print(res)
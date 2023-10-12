n = int(input())
max_st = list(map(int, input().split()))
res, day = 0, 0

for s in max_st:
    if s == 0:
        res = max(day, res)
        day = 0
        continue
    day += 1
res = max(day, res)

print(res)
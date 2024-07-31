t, d, m = map(int, input().split())
now, res = 0, "N"

for _ in range(m):
    y = int(input())

    if y - now >= t:
        res = "Y"
        break
    now = y
if d - now >= t:
    res = "Y"

print(res)
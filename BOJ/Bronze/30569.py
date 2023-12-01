from math import ceil
h1, d1, t1 = map(int, input().split())
h2, d2, t2 = map(int, input().split())

res1 = ceil((h2 - d1) / d1) * t1
res2 = ceil((h1 - d2) / d2) * t2

if res1 < res2:
    print("player one")
elif res1 > res2:
    print("player two")
else:
    print("draw")
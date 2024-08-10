from math import lcm
res = 1e9

for _ in range(int(input())):
    y, c1, c2 = map(int, input().split())
    res = min(y + lcm(c1, c2), res)

print(res)

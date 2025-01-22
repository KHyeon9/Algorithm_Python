from itertools import combinations

n, m = map(int, input().split())
house, chicken = [], []
res = 0

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            house.append((i, j))
        elif line[j] == 2:
            chicken.append((i, j))

chicken_com = combinations(chicken, m)
res = 1e9

for com in chicken_com:
    total = 0
    for h_p in house:
        min_len = 1e9
        for c_p in com:
            h_y, h_x = h_p
            c_y, c_x = c_p
            chicken_len = abs(c_y - h_y) + abs(c_x - h_x)
            min_len = min(chicken_len, min_len)
        total += min_len
    res = min(res, total)
print(res)
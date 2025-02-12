n = int(input())
s_x, s_y, e_x, e_y = map(int, input().split())
res = []

for _ in range(n):
    m = int(input())
    points = [list(map(int, input().split())) for _ in range(m)]
    points.append([e_x, e_y])
    now_x, now_y = s_x, s_y
    total = 0

    for point in points:
        total += abs(now_x - point[0]) + abs(now_y - point[1])
        now_x, now_y = point[0], point[1]

    res.append(total)

print(res.index(min(res)) + 1)

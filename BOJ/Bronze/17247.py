n, m = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(n)]
xy = []
for i in range(n):
    for j in range(m):
        if d[i][j] == 1:
            xy.append([i, j])
print(abs(xy[0][0] - xy[1][0]) + abs(xy[0][1] - xy[1][1]))

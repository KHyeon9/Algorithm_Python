from math import sqrt

res = 1e9
t = int(input())
arr = [list(map(int, input().split())) for _ in range(t)]

for i in range(t):
    x, y = arr[i][0], arr[i][1]
    temp = 0
    for j in range(t):
        if i == j:
            continue
        x2, y2 = arr[j][0], arr[j][1]
        temp += sqrt((x - x2) ** 2 + (y - y2) ** 2)

    temp /= (t - 1)
    res = min(res, temp)

print(res)


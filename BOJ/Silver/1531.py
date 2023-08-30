arr = [[0] * 101 for _ in range(101)]
res = 0

n, m = map(int, input().split())

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            arr[i][j] += 1

for i in range(1, 101):
    for j in range(1, 101):
        if arr[i][j] > m:
            res += 1

print(res)
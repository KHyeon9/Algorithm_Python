n = int(input())
num = int(input())
l = n
arr = [[0] * n for _ in range(n)]
move = 1
i = n ** 2
x, y = -1, 0
while i >= 1:
    for _ in range(n):
        x += move
        arr[x][y] = i
        i -= 1
    n -= 1

    for _ in range(n):
        y += move
        arr[x][y] = i
        i -= 1
    move *= -1

for i in arr:
    print(*i)

for i in range(l):
    for j in range(l):
        if arr[i][j] == num:
            print(i + 1, j + 1)
            exit()
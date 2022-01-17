def sol(x, y, num):
    color = arr[x][y]
    for i in range(x, x + num):
        for j in range(y, y + num):
            if color != arr[i][j]:
                sol(x, y, num // 2)
                sol(x, y + num // 2, num // 2)
                sol(x + num // 2, y, num // 2)
                sol(x + num // 2, y + num // 2, num // 2)
                return
    if color == 0:
        result[0] += 1
    else:
        result[1] += 1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [0, 0]
sol(0, 0, n)
print(result[0])
print(result[1])


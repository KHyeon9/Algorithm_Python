def sol(x, y, N):
    number = arr[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if number != arr[i][j]:
                for X in range(3):
                    for Y in range(3):
                        sol(x + X * (N // 3), y + Y * (N // 3), N // 3)
                return
    if number == -1:
        result[0] += 1
    elif number == 0:
        result[1] += 1
    else:
        result[2] += 1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [0, 0, 0]
sol(0, 0, n)
print(result[0])
print(result[1])
print(result[2])
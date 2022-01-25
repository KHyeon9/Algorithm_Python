def sol(x, y, num):
    color = arr[x][y]
    for i in range(x, x + num):
        for j in range(y, y + num):
            if color != arr[i][j]:
                print('(', end='')
                sol(x, y, num // 2)
                sol(x, y + num // 2, num // 2)
                sol(x + num // 2, y, num // 2)
                sol(x + num // 2, y + num // 2, num // 2)
                print(')', end='')
                return
    if color == 1:
        print(1, end='')
    else:
        print(0, end='')


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
sol(0, 0, n)

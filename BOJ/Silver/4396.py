def search(x, y, arr, l):
    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]
    cnt = 0
    for i in range(9):
        if 0 <= x + dx[i] < l and 0 <= y + dy[i] < l:
            if arr[x + dx[i]][y + dy[i]] == '*':
                cnt += 1
    return cnt


def game(arr, arr2, l, f):
    answer = []

    for i in range(l):
        line = []
        for j in range(l):
            if arr[i][j] == 'x':
                if arr2[i][j] == '*' and not f:
                    f = True
                    return game(arr, arr2, l, f)

                if arr2[i][j] == '*':
                    line.append(arr2[i][j])
                else:
                    line.append(search(i, j, arr2, l))
            else:
                if f:
                    line.append(arr2[i][j])
                else:
                    line.append('.')
        answer.append(line)

    return answer


n = int(input())
mine = [input() for _ in range(n)]
click = [input() for _ in range(n)]
flag = False
result = game(click, mine, n, flag)
for i in result:
    print(*i, sep='')

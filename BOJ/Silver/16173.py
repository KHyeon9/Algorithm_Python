from collections import deque


def bfs(x, y):
    queue = deque([[x, y]])
    while queue:
        x, y = queue.popleft()
        if arr[x][y] == -1:
            return True
        for i in range(2):
            X, Y = x + (i * arr[x][y]), y + ((1 - i) * arr[x][y])
            if 0 <= X < n and 0 <= Y < n and not visited[X][Y]:
                visited[X][Y] = True
                queue.append([X, Y])
    return False


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

if bfs(0, 0):
    print('HaruHaru')
else:
    print('Hing')
def bfs(x, y):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = [(x, y)]
    while queue:
        a, b = queue.pop(0)
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and Map[nx][ny] == 1:
                Map[nx][ny] = Map[a][b] + 1
                queue.append((nx, ny))

    return Map[-1][-1]


n, m = map(int, input().split())
Map = [list(map(int, input())) for _ in range(n)]
print(bfs(0, 0))

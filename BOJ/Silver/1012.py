from collections import deque


def bfs(X, Y):
    queue = deque([[X, Y]])
    move_x, move_y = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            moved_x = a + move_x[i]
            moved_y = b + move_y[i]
            if 0 <= moved_x < n and 0 <= moved_y < m and graph[moved_x][moved_y] == 1:
                graph[moved_x][moved_y] = 0
                queue.append([moved_x, moved_y])


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * m for i in range(n)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i, j)
                graph[i][j] = 0
                cnt += 1
    print(cnt)

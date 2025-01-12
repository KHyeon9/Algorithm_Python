from collections import deque

n, m = map(int, input().split())
board = []
visit = [[-1] * m for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

for i in range(n):
    line = list(map(int, input().split()))
    board.append(line)

    for j in range(m):
        if line[j] == 2:
            start_y, start_x = i, j
            visit[start_y][start_x] = 0
        if line[j] == 0:
            visit[i][j] = 0


def bfs():
    deq = deque([(start_y, start_x)])

    while deq:
        y, x = deq.popleft()

        for i in range(4):
            nxt_y = y + dy[i]
            nxt_x = x + dx[i]

            if not (0 <= nxt_y < n and 0 <= nxt_x < m):
                continue

            if board[nxt_y][nxt_x] == 0 or visit[nxt_y][nxt_x] != -1:
                continue

            visit[nxt_y][nxt_x] = visit[y][x] + 1
            deq.append((nxt_y, nxt_x))

bfs()

for el in visit:
    print(*el)

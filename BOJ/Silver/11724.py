from collections import deque
from sys import stdin


def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        start = queue.popleft()
        for i in range(1, n + 1):
            if not visited[i] and graph[start][i] == 1:
                queue.append(i)
                visited[i] = True


n, m = map(int, stdin.readline().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    u, v = map(int, stdin.readline().split())
    graph[u][v] = 1
    graph[v][u] = 1
c = 0
for j in range(1, n + 1):
    if not visited[j]:
        bfs(j)
        c += 1
print(c)



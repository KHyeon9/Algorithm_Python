from collections import deque


def dfs(start):
    visited[start] = True
    print(start, end=' ')
    for i in range(1, n + 1):
        if not visited[i] and graph[start][i] == 1:
            dfs(i)


def bfs(start):
    queue = deque([start])
    visited2[start] = True
    while queue:
        start = queue.popleft()
        print(start, end=' ')
        for i in range(1, n + 1):
            if not visited2[i] and graph[start][i] == 1:
                queue.append(i)
                visited2[i] = True


n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
visited2 = [False] * (n + 1)
cnt = n
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
dfs(v)
print()
bfs(v)


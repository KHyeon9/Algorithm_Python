def dfs(start):
    visited[start] = True

    for i in range(1, n + 1):
        if not visited[i] and graph[start][i] == 1:
            dfs(i)


n, m = map(int, input().split())
visited = [False] * (n + 1)
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
dfs(1)
if False in visited[1:]:
    for i in range(1, n + 1):
        if not visited[i]:
            print(i)
else:
    print(0)
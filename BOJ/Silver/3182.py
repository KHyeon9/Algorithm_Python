def dfs(start, cnt):
    visited[start] = True
    g = graph[start][0]
    if not visited[g]:
        cnt = dfs(g, cnt + 1)
    return cnt


n = int(input())
graph = [[] for _ in range(n + 1)]
result = [0] * (n + 1)
for i in range(1, n + 1):
    h = int(input())
    graph[i].append(h)

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    result[i] = dfs(i, 1)

print(result.index(max(result)))
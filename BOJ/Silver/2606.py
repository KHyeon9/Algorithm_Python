def dfs(start):
    visited[start] = True
    result.append(start)
    for i in range(1, n + 1):
        if not visited[i] and arr[start][i]:
            dfs(i)
    return result


n = int(input())
m = int(input())
arr = [[0] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
result = []
for _ in range(m):
    u, v = map(int, input().split())
    arr[u][v] = 1
    arr[v][u] = 1

print(len(dfs(1)) - 1)
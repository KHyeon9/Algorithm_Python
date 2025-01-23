from collections import deque

n, m = map(int, input().split())
users = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    users[a].append(b)
    users[b].append(a)

kevin = []

def bfs(start, goal):
    visited = [False] * (n + 1)
    visited[start] = True
    dq = deque([(start, 0)])

    while dq:
        now, d = dq.popleft()

        if now == goal:
            return d

        for nxt in users[now]:
            if not visited[nxt]:
                visited[nxt] = True
                dq.append((nxt, d + 1))

def get_kevin(start):
    ans = 0

    for i in range(1, n + 1):
        if i != start:
            ans += bfs(start, i)

    return ans

for i in range(1, n + 1):
    kevin.append(get_kevin(i))

print(kevin.index(min(kevin)) + 1)
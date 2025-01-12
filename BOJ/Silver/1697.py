from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001

def dfs(now):
    deq = deque()
    deq.append(now)

    while deq:
        num = deq.popleft()

        if num == k:
            print(visited[num])
            return

        for nxt in [num - 1, num + 1, num * 2]:
            if 0 <= nxt <= 100000 and not visited[nxt]:
                visited[nxt] = visited[num] + 1
                deq.append(nxt)

dfs(n)
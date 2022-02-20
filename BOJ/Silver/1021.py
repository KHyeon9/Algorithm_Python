from collections import deque
from sys import stdin
read = stdin.readline
n, m = map(int, read().split())
nums = list(map(int, read().split()))

que = deque(list(i for i in range(1, n + 1)))
cnt = 0

for num in nums:
    for i in range(n):
        if que[0] == num:
            que.popleft()
            break
        elif que.index(num) < len(que) / 2:
            while que[0] != num:
                que.append(que.popleft())
                cnt += 1
        else:
            while que[0] != num:
                que.appendleft(que.pop())
                cnt += 1
print(cnt)

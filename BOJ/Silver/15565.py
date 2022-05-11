from collections import deque
n, k = map(int, input().split())
doll = list(map(int, input().split()))
queue = deque()
step = k * 2 + 1
cnt, ryan = 0, 0
result = 1e9

for i in range(n):
    queue.append(doll[i])

    if step < cnt:
        if queue.popleft() == 1:
            ryan -= 1

    if doll[i] == 1:
        ryan += 1
        cnt += 1
    elif doll[i] == 2:
        cnt += 1

    while ryan == k:
        result = min(len(queue), result)
        if queue.popleft() == 1:
            ryan -= 1

print(result if result != 1e9 else -1)
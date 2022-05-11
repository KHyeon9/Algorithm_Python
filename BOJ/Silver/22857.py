from collections import deque

n, k = map(int, input().split())
S = list(map(int, input().split()))
q = deque()
delete, l, cnt, max_cnt = 0, 0, 0, 0

for i in S:
    q.append(i)

    if i % 2 == 0:
        cnt += 1
    else:
        delete += 1
    if delete > k:
        num = q.popleft()
        if num % 2 == 1:
            delete -= 1
        else:
            cnt -= 1
    if len(q) > l and cnt > max_cnt:
        l = len(q)
        max_cnt = cnt

print(max_cnt)
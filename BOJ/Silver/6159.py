n, s = map(int, input().split())
cow = sorted([int(input()) for _ in range(n)])
start, end = 0, 1
cnt = 0
while start < n and end < n:

    total = cow[start] + cow[end]
    if total <= s:
        cnt += 1
    end += 1
    if end >= n:
        start += 1
        end = start + 1

print(cnt)
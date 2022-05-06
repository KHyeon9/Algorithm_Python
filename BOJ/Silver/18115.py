from collections import deque

n = int(input())
tech = list(map(int, input().split()))
tech.reverse()
result = deque()

for i in range(n):
    if tech[i] == 1:
        result.appendleft(i + 1)
    elif tech[i] == 2:
        result.insert(1, i + 1)
    else:
        result.append(i + 1)
print(*result)


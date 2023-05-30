n, m = map(int, input().split())

travel = [0] * m
res = []

for _ in range(n):
    students = list(map(int, input().split()))

    for i in range(m):
        if students[i] == 1:
            travel[i] += 1

for i in range(max(travel), -1, -1):
    for j in range(m):
        if i == travel[j]:
            res.append(j + 1)
print(*res)
w, p = map(int, input().split())
res = []
partition = [0] + list(map(int, input().split())) + [w]


for i in range(len(partition) - 1):
    for j in range(i + 1, len(partition)):
        res.append(partition[j] - partition[i])

print(*sorted(set(res)))

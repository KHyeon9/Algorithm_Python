n, m = map(int, input().split())
pl = [list(map(int, input().split())) for _ in range(n)]
result = 0

for i in range(n):
    pl_sort = sorted(pl[i])
    temp = []
    for j in pl[i]:
        temp.append(pl_sort.index(j))
    pl[i] = temp

for i in range(n):
    for j in range(i + 1, n):
        if pl[i] == pl[j]:
            result += 1
print(result)


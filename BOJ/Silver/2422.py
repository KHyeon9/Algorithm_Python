n, m = map(int, input().split())
ice_no = {i: [] for i in range(1, n + 1)}
result = 0
for _ in range(m):
    a, b = map(int, input().split())
    ice_no[a].append(b)
    ice_no[b].append(a)
for i in range(1, n - 1):
    for j in range(i + 1, n):
        if j in ice_no[i]:
            continue
        for k in range(j + 1, n + 1):
            if k in ice_no[i] or k in ice_no[j]:
                continue
            result += 1
print(result)





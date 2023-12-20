t = int(input())
for _ in range(t):
    group = list(map(int, input().split()))
    n = group[0]
    group = group[1:]
    num = group[0]
    res = -1

    for i in range(n):
        if num != group[i]:
            res = i + 1
            break
        num += 1

    print(res)
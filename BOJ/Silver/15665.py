def sol(n, m):
    if len(r) == m:
        print(*r)
        return
    for i in arr2:
        r.append(i)
        sol(n, m)
        r.pop()


r = []
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
arr2 = sorted(list(set(arr)))
sol(N, M)
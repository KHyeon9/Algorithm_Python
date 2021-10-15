def sol(n, m):
    if len(r) == m:
        print(*r)
        return
    for i in range(n):
        r.append(arr[i])
        sol(n, m)
        r.pop()


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
r = []
sol(N, M)
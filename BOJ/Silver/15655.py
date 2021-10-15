def sol(n, m, c):
    if len(r) == m:
        if r == sorted(r):
            print(*r)
        return
    for i in range(c, n):
        if arr[i] not in r:
            r.append(arr[i])
            sol(n, m, c)
            c += 1
            r.pop()


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
r = []
sol(N, M, 0)
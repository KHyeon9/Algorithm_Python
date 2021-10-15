def sol(n, m, c):
    if len(r) == m:
        print(*r)
        return
    for i in range(c, n):
        r.append(arr[i])
        sol(n, m, c)
        c += 1
        r.pop()


r = []
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
sol(N, M, 0)
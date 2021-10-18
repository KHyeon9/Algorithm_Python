def sol(n, m):
    if len(r) == m:
        print(*r)
        return
    for i in arr2:
        if i not in r or arr.count(i) > 1:
            if arr.count(i) <= r.count(i):
                continue
            r.append(i)
            sol(n, m)
            r.pop()


r = []
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
arr2 = sorted(list(set(arr)))
sol(N, M)

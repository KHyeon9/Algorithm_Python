def sol(a, b):
    if len(r) == b:
        print(*r)
        return
    for i in range(a):
        if arr[i] not in r:
            r.append(arr[i])
            sol(a, b)
            r.pop()


n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
r = []
sol(n, m)
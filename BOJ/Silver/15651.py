def sol(c, l):
    if len(arr) == l:
        print(*arr)
        return
    for i in range(1, c + 1):
        arr.append(i)
        sol(c, l)
        arr.pop()


m, n = map(int, input().split())
arr = []
sol(m, n)
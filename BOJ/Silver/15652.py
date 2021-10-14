def sol(a, b, cnt):
    if len(arr) == b:
        print(*arr)
        return
    for i in range(cnt, a + 1):
        arr.append(i)
        sol(a, b, cnt)
        cnt += 1
        arr.pop()


arr = []
n, m = map(int, input().split())
sol(n, m, 1)
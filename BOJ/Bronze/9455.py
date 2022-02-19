for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    r = 0
    for i in range(m):
        arr2 = []
        for j in range(n):
            arr2.append(arr[j][i])
        for k in range(n):
            if arr2[k] == 1:
                r += arr2[k:].count(0)
    print(r)

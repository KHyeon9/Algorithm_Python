for _ in range(int(input())):
    input()
    n, e = map(int, input().split())
    que = [i for i in range(1, n + 1)]
    for _ in range(e):
        p = que.pop(que.index(int(input())))
        que.insert(0, p)

    print(que[-1])
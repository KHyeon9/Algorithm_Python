while 1:
    n = list(map(int, input().split()))

    if n[0] == 0:
        break

    for i in range(n[0] // 4):
        a = [2 * i + 1, 2 * i + 2, n[0] - (2 * i + 1), n[0] - (i * 2)]
        if n[1] in a:
            a.remove(n[1])
            print(*a)
            break
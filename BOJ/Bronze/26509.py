for _ in range(int(input())):
    tri1 = sorted(list(map(int, input().split())))
    tri2 = sorted(list(map(int, input().split())))

    res = "NO"

    if tri1 == tri2 and tri1[0] ** 2 + tri1[1] ** 2 == tri1[2] ** 2:
        res = "YES"

    print(res)
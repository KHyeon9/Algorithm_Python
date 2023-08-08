while True:
    n, m = map(int, input().split())

    if n == m == 0:
        break

    res = [0] * 10

    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    for a in a_list:
        for b in b_list:
            num = str(a * b)
            for n in num:
                res[int(n)] += 1

    print(*res)


while 1:
    n = int(input())
    if n == 0:
        break

    n1, n2, n3 = map(int, input().split())

    if n2 - n1 == n3 - n2:
        d = n2 - n1
        res = n * (2 * n1 + (n - 1) * d) // 2
    else:
        r = n2 // n1
        res = n1 * ((r ** n - 1) // (r - 1))
    print(res)
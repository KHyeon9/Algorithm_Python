while 1:
    a, b = list(map(int, input().split()))

    if a == 0 and b == 0:
        break

    else:
        r1 = a // b
        r2 = a % b

        print(r1, r2, "/", b)
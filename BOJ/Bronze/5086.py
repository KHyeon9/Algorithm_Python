while 1:
    n1, n2 = list(map(int, input().split()))

    if n1 == 0 and n2 == 0:
        break

    else:
        if n1 % n2 == 0:
            print("multiple")

        elif n2 % n1 == 0:
            print("factor")

        else:
            print("neither")
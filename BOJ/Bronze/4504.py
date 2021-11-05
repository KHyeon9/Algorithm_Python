n = int(input())

while 1:
    n2 = int(input())

    if n2 == 0:
        break

    else:
        if n2 // n > 0 and n2 % n == 0:
            print("{} is a multiple of {}.".format(n2, n))

        else:
            print("{} is NOT a multiple of {}.".format(n2, n))
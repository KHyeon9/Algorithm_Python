while 1:
    n = int(input())

    if n == 0:
        break

    else:
        while n // 10 != 0:
            n = n // 10 + n % 10

        print(n)
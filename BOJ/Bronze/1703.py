while True:
    a = list(map(int, input().split()))

    if a[0] == 0:
        break
    else:
        if a[0] == 1:
            r = a[1] - a[2]
            print(r)

        else:
            r = 1
            for i in range(1, a[0] * 2 + 1):
                if i % 2 == 1:
                    r *= a[i]

                elif i % 2 == 0:
                    r -= a[i]

            print(r)

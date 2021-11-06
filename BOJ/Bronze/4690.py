for i in range(6, 101):
    n = i ** 3
    for j in range(2, i):
        n1 = j ** 3
        for k in range(j + 1, i):
            n2 = k ** 3
            for l in range(k + 1, i):
                n3 = l ** 3
                if n == n1 + n2 + n3:
                    print("Cube = %d, Triple = (%d,%d,%d)" % (i, j, k, l))
                
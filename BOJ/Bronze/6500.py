while True:
    a = int(input())

    if a == 0:
        break

    res = [a]

    while True:
        a = str(a ** 2)
        a = int(('0' * (8 - len(a)) + a)[2:-2])
        if a in res:
            break
        res.append(a)

    print(len(res))

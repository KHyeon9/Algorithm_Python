while 1:
    heisei = list(input().split())

    if heisei[0] == '#':
        break

    for i in range(1, len(heisei)):
        heisei[i] = int(heisei[i])

    if heisei[1] > 31:
        heisei[0] = '?'
        heisei[1] -= 30

    elif heisei[1] == 31 and heisei[2] >= 5:
        heisei[0] = '?'
        heisei[1] -= 30
    print(*heisei)

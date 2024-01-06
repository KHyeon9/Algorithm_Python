for _ in range(int(input())):
    n = list(str(int(input()) + 1))

    for i in range(len(n)):
        if n[i] == '0':
            n[i] = '1'

    print(*n, sep='')
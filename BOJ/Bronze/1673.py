while 1:
    try:
        n, k = map(int, input().split())
        plus, temp = n, 0
        while plus // k:
            temp = plus // k
            temp2 = plus % k
            n += temp
            plus = temp + temp2

        print(n)
    except EOFError:
        break

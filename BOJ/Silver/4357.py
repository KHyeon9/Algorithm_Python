while 1:
    try:
        num = int(input())
        n = '1'
        while 1:
            if int(n) % num == 0:
                print(len(n))
                break
            n += '1'
    except EOFError:
        break
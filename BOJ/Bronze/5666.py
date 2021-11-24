while 1:
    try:
        h, p = map(int, input().split())
        print('%.2f' % (h / p))
    except EOFError:
        break

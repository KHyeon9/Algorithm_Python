res = 0
while 1:
    try:
        s = input()
        res += 1
    except EOFError:
        print(res)
        break
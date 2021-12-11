while 1:
    l, w, a = map(int, input().split())

    if l == w == a == 0:
        break

    if l == 0:
        print(a // w, w, a)

    elif w == 0:
        print(l, a // l, a)

    else:
        print(l, w, l * w)
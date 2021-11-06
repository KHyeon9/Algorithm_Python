a = float(input())

while 1:
    t = float(input())

    if t == 999:
        break

    else:
        r = t - a
        print("%.2f" % r)
        a = t
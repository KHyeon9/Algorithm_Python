for _ in range(int(input())):
    p, d, c, b = input().split()
    p = float(p)

    if d == 'R':
        p *= 0.55
    elif d == 'G':
        p *= 0.7
    elif d == 'B':
        p *= 0.8
    elif d == 'Y':
        p *= 0.85
    elif d == 'O':
        p *= 0.9
    elif d == 'W':
        p *= 0.95

    if c == 'C':
        p *= 0.95

    if b == 'P':
        print("$%.2f" % p)
    else:
        p -= 0.01
        print("$%.2f" % round(p, 1))

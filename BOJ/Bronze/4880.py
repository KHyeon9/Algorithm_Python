while 1:
    a, b, c = list(map(int, input().split()))
    n1 = b - a
    n2 = c - b
    
    if a == b == c == 0:
        break

    elif n1 == n2:
        print("AP", c + n1)

    else:
        s = b // a
        print("GP", c * s)
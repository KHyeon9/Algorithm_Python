for _ in range(int(input())):
    n, tran = input().split()
    n = float(n)
    if tran == "kg":
        print("%.4f lb" % (n * 2.2046))
    elif tran == "lb":
        print("%.4f kg" % (n * 0.4536))
    elif tran == "l":
        print("%.4f g" % (n * 0.2642))
    else:
        print("%.4f l" % (n * 3.7854))
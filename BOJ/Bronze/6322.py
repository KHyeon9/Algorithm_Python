from math import sqrt
i = 1
while 1:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    print(f"Triangle #{i}")
    if a == -1:
        if b ** 2 >= c ** 2:
            print("Impossible.")
        else:
            print("a = %.3f" % sqrt(c ** 2 - b ** 2))
    elif b == -1:
        if a ** 2 >= c ** 2:
            print("Impossible.")
        else:
            print("b = %.3f" % sqrt(c ** 2 - a ** 2))
    elif c == -1:
        print("c = %.3f" % sqrt(a ** 2 + b ** 2))
    i += 1
    print()
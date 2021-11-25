n = 1
while 1:
    a, b = map(int, input().split())

    if a == b == 0:
        break

    print("Hole #{}".format(n))

    if a == b:
        print("Par.")
    elif b == 1:
        print("Hole-in-one.")
    elif b == a - 1:
        print("Birdie.")
    elif b == a - 2:
        print("Eagle.")
    elif b == a - 3:
        print("Double eagle.")
    elif b == a + 1:
        print("Bogey.")
    else:
        print("Double Bogey.")
    print()

    n += 1
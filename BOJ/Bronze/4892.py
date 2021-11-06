num = 0

while 1:
    n = int(input())
    num += 1

    if n == 0:
        break

    n1 = 3 * n

    if n1 % 2 == 0:
        n2 = n1 / 2

    else:
        n2 = (n1 + 1) / 2

    r = int((3 * n2) // 9)

    if n1 % 2 == 0:
        print("{}. even {}".format(num, r))
    else:
        print("{}. odd {}".format(num, r))
from sys import stdin

while 1:
    n = int(stdin.readline())

    if n == 0:
        break

    r = n ** 2 - n + 1

    print(n, "=>", r)
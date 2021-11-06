from sys import stdin

while 1:
    n = int(stdin.readline())
    r = 0
    t = 0

    if n == -1:
        break

    for i in range(n):
        s, t1 = list(map(int, stdin.readline().split()))
        r += s * (t1 - t)
        t = t1

    print(r, "miles")
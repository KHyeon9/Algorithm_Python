from sys import stdin

for _ in range(int(stdin.readline())):
    x, w = map(int, stdin.readline().split())
    res = 0

    while x < w:
        x *= 2
        res += 1

    print(res)
from sys import stdin

for i in range(3):
    n = int(stdin.readline())

    r = [int(stdin.readline()) for _ in range(n)]

    if sum(r) > 0:
        print("+")
    elif sum(r) < 0:
        print("-")
    else:
        print(0)
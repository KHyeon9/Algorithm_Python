from math import sqrt

for _ in range(int(input())):
    n = int(input())

    if sqrt(n) == int(sqrt(n)):
        print(1)
    else:
        print(0)
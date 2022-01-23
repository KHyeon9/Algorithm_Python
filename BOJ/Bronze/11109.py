t = int(input())

for i in range(t):
    d, n, s, p = list(map(int, input().split()))

    r1 = d + n * p
    r2 = n * s

    if r1 < r2:
        print("parallelize")

    elif r1 > r2:
        print("do not parallelize")

    else:
        print("does not matter")
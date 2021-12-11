t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    r = 0

    for j in range(n):
        v, f, c = list(map(int, input().split()))

        a = m / v

        if c * a <= f:
            r += 1

    print(r)
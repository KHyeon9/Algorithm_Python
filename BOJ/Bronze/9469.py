t = int(input())

for i in range(t):
    n, d, a, b, f = list(map(float, input().split()))

    r = d / (a + b) * f

    print(int(n), "%.6f" % r)
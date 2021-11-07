n = int(input())
p = [350.34, 230.90, 190.55, 125.30, 180.90]

for i in range(n):
    a, b, c, d, e = map(int, input().split())
    r = a * p[0] + b * p[1] + c * p[2] + d * p[3] + e * p[4]

    print("$%.2f" % r)
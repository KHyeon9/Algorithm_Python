t = int(input())

for i in range(t):
    n = int(input())
    r1 = 0
    r2 = 0

    for j in range(n):
        c, g = map(float, input().split())
        r1 += c
        r2 += c * g

    print(int(r1), round(r2 / r1, 1))
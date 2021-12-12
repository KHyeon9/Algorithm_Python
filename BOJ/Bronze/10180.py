t = int(input())

for i in range(t):
    n, d = map(int, input().split())
    r = 0
    for j in range(n):
        v, f, c = map(int, input().split())
        k = d / v * c
        if k <= f:
            r += 1
    print(r)
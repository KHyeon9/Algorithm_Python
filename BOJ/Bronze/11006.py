t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))

    r1 = m * 2 - n
    r2 = m - r1

    print(r1, r2)
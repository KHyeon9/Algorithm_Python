t = int(input())

for _ in range(t):
    n = list(map(int, input().split()))
    r1 = 0
    r2 = 0

    for i in range(1, n[0] + 1):
        if n[i] % 2 == 0:
            r1 += n[i]
        else:
            r2 += n[i]

    if r1 > r2:
        print("EVEN")
    elif r1 < r2:
        print("ODD")
    else:
        print("TIE")
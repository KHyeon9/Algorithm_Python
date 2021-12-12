t = int(input())

for i in range(t):
    r1 = 0
    r2 = 0

    for j in range(9):
        y, k = map(float, input().split())
        r1 += y
        r2 += k

    if r1 > r2:
        print("Yonsei")

    elif r1 < r2:
        print("Korea")

    else:
        print("Draw")
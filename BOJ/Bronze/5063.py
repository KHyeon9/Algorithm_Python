t = int(input())

for i in range(t):
    r, e, c = list(map(int, input().split()))

    if r < e - c:
        print("advertise")

    elif r > e - c:
        print("do not advertise")

    else:
        print("does not matter")
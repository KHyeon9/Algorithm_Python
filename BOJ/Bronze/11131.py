t = int(input())

for _ in range(t):
    n = int(input())
    w = list(map(int, input().split()))
    s = sum(w)

    if s > 0:
        print("Right")
    elif s < 0:
        print("Left")
    else:
        print("Equilibrium")
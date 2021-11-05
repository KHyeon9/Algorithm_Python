t = int(input())

for i in range(t):
    n = int(input())
    r1 = r2 = 0
    
    for j in range(n):
        p1, p2 = input().split()

        if p1 == p2:
            continue

        elif (p1 == 'R' and p2 == 'P') or (p1 == 'S' and p2 == 'R') or (p1 == 'P' and p2 == 'S'):
            r2 += 1

        else:
            r1 += 1

    if r1 > r2:
        print("Player 1")
    elif r1 < r2:
        print("Player 2")
    else:
        print("TIE")
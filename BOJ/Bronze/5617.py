r1 = r2 = r3 = r4 = 0

while 1:
    n = list(map(int, input().split()))
    n.sort()
    if n[0] + n[1] <= n[2]:
        break

    else:
        r1 += 1
        if n[2] ** 2 == n[0] ** 2 + n[1] ** 2:
            r2 += 1
        elif n[2] ** 2 < n[0] ** 2 + n[1] ** 2:
            r3 += 1
        else:
            r4 += 1

print(r1, r2, r3, r4)
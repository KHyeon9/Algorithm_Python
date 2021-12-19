t = int(input())

for i in range(t):
    a = int(input())
    r = 0

    while 1:
        if a == 1:
            r = 0
            break
        elif (r + 1) + (r + 1) ** 2 <= a:
            r += 1
        else:
            break

    print(r)

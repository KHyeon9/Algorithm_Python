res = [0] * 4
for _ in range(int(input())):
    g, c, n = map(int, input().split())

    if g == 1:
        res[3] += 1
    elif c == 1 or c == 2:
        res[0] += 1
    elif c == 3:
        res[1] += 1
    else:
        res[2] += 1

for i in res:
    print(i)
t = int(input())

for i in range(t):
    n = int(input())
    r = 0
    for j in range(n + 1):
        if j % 2 == 1:
            r += j
    print(r)
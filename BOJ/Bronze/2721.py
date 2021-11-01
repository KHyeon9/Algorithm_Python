t = int(input())

for i in range(t):
    n = int(input())
    r = 0

    for j in range(2, n + 2):
        r += j * (j + 1) // 2 * (j - 1)

    print(r)
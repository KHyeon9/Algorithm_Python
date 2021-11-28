from sys import stdin
t = int(stdin.readline())

for i in range(t):
    n, m = list(map(int, stdin.readline().split()))
    r = 0
    for j in range(1, n):
        for k in range(j + 1, n):
            if (j ** 2 + k ** 2 + m) % (j * k) == 0:
                r += 1
    print(r)
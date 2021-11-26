n, m, p = map(int, input().split())
r = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if (i + j) * 2 >= p:
            r += (n - i + 1) * (m - j + 1)
print(r)
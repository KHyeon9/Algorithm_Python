from sys import stdin
n = int(stdin.readline())
res = 0

for i in range(1, n + 1):
    for j in range(i, n + 1):
        k = n - i - j
        if k < j:
            break
        if k < i + j:
            res += 1
print(res)
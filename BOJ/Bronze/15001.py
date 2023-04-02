from sys import stdin
input = stdin.readline
n = int(input())
d = [int(input()) for _ in range(n)]
res = 0

for i in range(1, n):
    res += (d[i] - d[i - 1]) ** 2
print(res)

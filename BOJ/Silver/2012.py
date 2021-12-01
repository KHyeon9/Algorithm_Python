from sys import stdin
input = stdin.readline
n = int(input())
arr = sorted([int(input()) for _ in range(n)])
r = 0
for i in range(1, n + 1):
    r += abs(arr[i - 1] - i)
print(r)
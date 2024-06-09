from math import sqrt
from sys import stdin
input = stdin.readline
res = 0
n, k, x, y = map(int, input().split())

for _ in range(n):
    xi, yi = map(int, input().split())
    if sqrt((xi - x) ** 2 + (yi - y) ** 2) > k:
        res += 1

print(res)
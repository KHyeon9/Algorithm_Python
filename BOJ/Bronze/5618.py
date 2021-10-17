from math import gcd
from sys import stdin
n = int(stdin.readline())
num = list(map(int, stdin.readline().split()))
G = gcd(num[0], gcd(num[1], num[-1]))
for i in range(1, G // 2 + 1):
    if G % i == 0:
        print(i)
print(G)
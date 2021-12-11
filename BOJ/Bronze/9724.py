from sys import stdin
from math import ceil
for i in range(int(input())):
    n1, n2 = map(int, stdin.readline().split())
    r = 0
    for j in range(int(n1 ** (1 / 3)), ceil(n2 ** (1 / 3))):
        if n1 <= j ** 3 <= n2:
            r += 1

    print(f"Case #{i + 1}: {r}")
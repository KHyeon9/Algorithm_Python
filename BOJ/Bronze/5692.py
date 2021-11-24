from math import factorial
from sys import stdin

while 1:
    n = stdin.readline().strip()
    s = 0
    if n == '0':
        break

    for i in range(len(n)):
        s += int(n[i]) * factorial(len(n) - i)

    print(s)
from math import ceil
n = int(input())
x, y = 0, ceil(n / 3)

while 2 * x + 3 * y != n:
    x += 1
    y -= 1

print(x, y)
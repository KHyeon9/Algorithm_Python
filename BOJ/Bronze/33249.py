from math import pi

d, h = map(float, input().split())
r = d / 2 + 5
print(pi * r ** 2 + 2 * pi * r * h)

from math import pi

a1, p1 = map(int, input().split())
r1, p2 = map(int, input().split())

r = p1 / a1
r2 = p2 / (r1 ** 2 * pi)

if r < r2:
    print("Slice of pizza")

else:
    print("Whole pizza")
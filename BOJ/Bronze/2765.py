import math
n = 1
while 1:
    d, r, s = map(float, input().split())
    if r == 0:
        break
    r = d * math.pi * r / 12 / 5280
    print("Trip #%d: %.2f %.2f" % (n, r, r / s * 3600))
    n += 1
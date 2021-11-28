import math
while 1:
    d, rh, rn = map(float, input().split())
    if d == rh == rn == 0:
        break
    w = 16 * d / math.sqrt(337)
    h = w * 9 / 16
    print("Horizontal DPI: %.2f" % (rh/w))
    print("Vertical DPI: %.2f" % (rn/h))
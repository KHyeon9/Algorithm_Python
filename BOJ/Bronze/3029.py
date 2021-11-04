h, m, s = list(map(int, input().split(':')))
h2, m2, s2 = list(map(int, input().split(':')))

rh = h2 - h
rm = m2 - m
rs = s2 - s

if rs < 0:
    rm -= 1
    rs += 60

if rm < 0:
    rh -= 1
    rm += 60

if rh < 0:
    rh += 24

if rh == rm == rs == 0:
    rh = 24

print("%.2d:%.2d:%.2d" % (rh, rm, rs))
ca, ba, pa = map(int, input().split())
cr, br, pr = map(int, input().split())

rc = cr - ca
rb = br - ba
rp = pr - pa

if rc > 0:
    rc = cr - ca

else:
    rc = 0

if rb > 0:
    rb = br - ba

else:
    rb = 0

if rp > 0:
    rp = pr - pa

else:
    rp = 0

print(rc + rb + rp)

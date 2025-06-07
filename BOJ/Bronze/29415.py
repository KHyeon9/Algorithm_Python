from math import sqrt

s = int(input())
extent = 2 * s
res = 0

for a in range(1, int(sqrt(extent)) + 1):
    if extent % a == 0:
        b = extent // a
        if a > b:
            break
        c_pow = a * a + b * b
        c = int(sqrt(c_pow))
        if c * c == c_pow:
            res += 1

print(res)

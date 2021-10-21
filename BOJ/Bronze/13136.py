r, c, n = map(int, input().split())
d1 = r // n
d2 = c // n
s = (r % n > 0) and 1 or 0
s2 = (c % n > 0) and 1 or 0

print((d1 + s) * (d2 + s2))
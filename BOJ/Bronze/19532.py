a, b, c, d, e, f = map(int, input().split())

x1 = a * e
y1 = b * d

x2 = b * d
y2 = a * e

minus_y = y1 - y2
minus_x = x1 - x2
y = (c * d - a * f) // minus_y
x = (c * e - b * f) // minus_x

print(x, y)


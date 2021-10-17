import math

A, B, C = list(map(int, input().split()))

m = math.sqrt(B ** 2 + C ** 2)
x = int(B * (A / m))
y = int(C * (A / m))

print(x, y)
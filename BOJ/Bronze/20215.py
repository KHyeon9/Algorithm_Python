import math

w, h = map(int, input().split())

r = w + h - math.sqrt(w ** 2 + h ** 2)

print(r)

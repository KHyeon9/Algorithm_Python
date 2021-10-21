import math
a, b = map(int, input().split())

s = b - a

if a / s <= 1:
    print(2)

else:
    print(math.ceil(b / s))
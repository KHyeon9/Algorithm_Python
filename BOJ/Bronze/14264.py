import math

l = int(input())

r = math.sqrt((l ** 2) - ((l / 2) ** 2))

print(round(l * r / 2, 9))
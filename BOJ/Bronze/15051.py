a = int(input())
b = int(input())
c = int(input())

min1 = min(b * 2 + c * 4, a * 2 + c * 2)
r = min(min1, a * 4 + b * 2)

print(r)
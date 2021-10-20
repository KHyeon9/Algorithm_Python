a = int(input())
b = int(input())
c = int(input())
d = int(input())
p = int(input())

if p <= c:
    r = b

else:
    r = b + (p - c) * d

print(min(r, a * p))
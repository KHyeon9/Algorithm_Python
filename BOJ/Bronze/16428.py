a, b = map(int, input().split())

r1 = a // b
r2 = a % b

if b < 0:
    if r2 == 0:
        r1 = a // b
    else:
        r1 = a // b + 1

    r2 = a - (b * r1)

print(r1)
print(abs(r2))
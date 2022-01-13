a, b = map(int, input().split())
r1 = abs(a // 2 * b - (a - (a // 2)) * b)
r2 = abs(a * (b // 2) - a * (b - (b // 2)))
if r1 <= r2:
    print(r1)
else:
    print(r2)

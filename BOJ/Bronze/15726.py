a, b, c = map(int, input().split())

r1 = int(a / b * c)
r2 = int(a * b / c)

print(max(r1, r2))

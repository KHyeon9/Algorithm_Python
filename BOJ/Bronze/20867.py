m, s, g = map(int, input().split())
a, b = map(float, input().split())
l, r = map(int, input().split())
result1 = m / s + r / b
result2 = m / g + l / a
print('friskus' if result1 > result2 else 'latmask')

n, h, v = map(int, input().split())

m1 = max(n - h, h)
m2 = max(n - v, v)

print(m1 * m2 * 4)

n1, n2 = map(int, input().split())
a, b = 100 - n1, 100 - n2
c = 100 - (a + b)
d = a * b
q, r = d // 100, d % 100
print(a, b, c, d, q, r)
print(c + q, r)

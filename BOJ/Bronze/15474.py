n, a, b, c, d = map(int, input().split())

p1 = n // a * b
p2 = n // c * d
l1 = n % a
l2 = n % c

if l1 != 0:
    p1 = (n // a + 1) * b

if l2 != 0:
    p2 = (n // c + 1) * d

print(min(p1, p2))
a, b, c, d = map(int, input().split())
h = list(map(int, input().split()))

d1 = a + b
d2 = c + d

for i in h:
    r = 0
    if 0 < i % d1 <= a:
        r += 1
    if 0 < i % d2 <= c:
        r += 1
    print(r)
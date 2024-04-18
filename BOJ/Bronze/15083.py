p1, p2, p3 = sorted(list(map(int, input().split())))
c1, c2, c3 = list(map(int, input().split()))

if c2 > c3:
    c2, c3 = c3, c2

v1 = (p1 + p2 + p3) * c1 / 100
v2 = p2 * c2 / 100 + p3 * c3 / 100

print(f"one {v1:.2f}" if v1 > v2 else f"two {v2:.2f}")
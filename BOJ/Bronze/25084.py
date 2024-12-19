from math import pi

for t in range(1, int(input()) + 1):
    r, a, b = map(int, input().split())
    res = 0

    while r > 0:
        res += pi * (r ** 2)
        r *= a
        res += pi * (r ** 2)
        r //= b

    print(f"Case #{t}: {res:.6f}")
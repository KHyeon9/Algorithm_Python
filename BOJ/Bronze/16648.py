t, p = map(int, input().split())

a = t / (100 - p)
b = t / ((20 - p) * 2 + 80)

if p <= 20:
    print(p * b * 2)

else:
    print(a * (p - 20) + (a * 2 * 20))
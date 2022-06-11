a, b = map(int, input().split())
d_ig = a / 100 * b
res = a - d_ig
if res >= 100:
    print(0)
else:
    print(1)
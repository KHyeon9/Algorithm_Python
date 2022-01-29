a, b, c = map(int, input().split())
r1 = (a + b - c) / 2
r2 = (a - b + c) / 2
r3 = (-a + b + c) / 2
if r1 > 0 and r2 > 0 and r3 > 0:
    print(1)
    print(r1, r2, r3)
else:
    print(-1)
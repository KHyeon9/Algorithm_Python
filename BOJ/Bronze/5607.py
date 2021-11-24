t = int(input())
r1 = r2 = 0

for _ in range(t):
    a, b = map(int, input().split())
    if a > b:
        r1 += a + b
    elif a < b:
        r2 += a + b
    else:
        r1 += a
        r2 += b
print(r1, r2)
a, b, c = map(int, input().split())
i, j, k = map(int, input().split())
cnt = min(a / i, b / j, c / k)
r1 = a - i * cnt
r2 = b - j * cnt
r3 = c - k * cnt
print(r1, r2, r3)
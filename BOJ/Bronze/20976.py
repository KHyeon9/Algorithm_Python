a, b, c = map(int, input().split())

s = a + b + c
m = max(a, b, c)
m2 = min(a, b, c)

print(s - m - m2)
a, b, c = map(int, input().split())

s = a + b + c
min = min(a, b, c)

print(s - min)

a, b, c, d = map(int, input().split())

t = max(a, b, c, d) + min(a, b, c, d)
r = (t * 2) - (a + b + c + d)

print(abs(r))
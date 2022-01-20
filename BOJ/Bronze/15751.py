a, b, x, y = map(int, input().split())
r = abs(max(a, b) - max(x, y)) + abs(min(a, b) - min(x, y))
print(r if r <= abs(a - b) else abs(a - b))
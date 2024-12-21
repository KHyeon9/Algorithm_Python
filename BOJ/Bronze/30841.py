a, b = map(int, input().split())

print((a * b) // (a + b) if a + b > 0 else 0)
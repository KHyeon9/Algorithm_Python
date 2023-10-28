n = int(input())
m = int(input())

print(min(n, m) * 2 + ((n + m) & 1))
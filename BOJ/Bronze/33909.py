s, c, o, n = map(int, input().split())
c += o * 2
n += s
print(min(n // 3, c // 6))
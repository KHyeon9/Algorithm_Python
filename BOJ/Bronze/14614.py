a, b, c = map(int, input().split())
print(a if c % 2 == 0  else a ^ b)
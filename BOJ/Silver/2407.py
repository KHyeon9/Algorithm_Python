from math import factorial
n, m = map(int, input().split())
r1 = factorial(n) // factorial(n - m)
r2 = factorial(m)
print(r1 // r2)
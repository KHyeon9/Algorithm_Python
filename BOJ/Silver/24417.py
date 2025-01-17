n = int(input())
mod = 1000000007
a, b = 1, 1

for i in range(2, n):
    a, b = b, (a + b) % mod

print(b, n - 2)
n = int(input())

for i in range(n - 1):
    print(" " * (n - i - 1) + "*" * (i * 2 + 1))
for i in range(n):
    print(" " * i + "*" * (n * 2 - (i * 2 + 1)))

from math import factorial

n = int(input())

if n < 5:
    print(0)
    exit()

print(factorial(n) // (factorial(5) * factorial(n - 5)))
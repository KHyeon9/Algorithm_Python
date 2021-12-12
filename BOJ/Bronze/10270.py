from math import factorial
mod = 1000000007
for _ in range(int(input())):
    n = int(input())
    print(factorial(n) % mod - 1)
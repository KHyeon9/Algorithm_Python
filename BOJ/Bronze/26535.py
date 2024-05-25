from math import sqrt, ceil
n = int(input())
k = ceil(sqrt(n))

print('x' * (k + 2))

for _ in range(k):
    print('x' + '.' * k + 'x')

print('x' * (k + 2))


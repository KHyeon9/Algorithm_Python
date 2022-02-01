from sys import stdin
from math import sqrt
read = stdin.readline
a, b = read().split()
num, num2 = int(a), int(b + a)
result = "Yes"
for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
        result = "No"
        break
for i in range(2, int(sqrt(num2)) + 1):
    if num2 % i == 0:
        result = "No"
        break
print(result)
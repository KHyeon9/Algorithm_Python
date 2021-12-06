from math import factorial
n = int(input())
num = str(factorial(n))
for i in range(len(num) - 1, -1, -1):
    if num[i] != '0':
        print(num[i])
        break

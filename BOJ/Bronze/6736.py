from math import factorial

for _ in range(int(input())):
    a, b = map(int, input().split())

    print(str(factorial(a)).count(str(b)))
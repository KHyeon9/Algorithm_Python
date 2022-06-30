from math import factorial
for _ in range(int(input())):
    n = int(input())
    fac = str(factorial(n))
    for i in fac[::-1]:
        i = int(i)
        if i != 0:
            print(i)
            break
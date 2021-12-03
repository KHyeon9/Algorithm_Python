from math import sqrt
def sol(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True
for _ in range(int(input())):
    n = int(input())
    while 1:
        if sol(n):
            print(n)
            break
        else:
            n += 1


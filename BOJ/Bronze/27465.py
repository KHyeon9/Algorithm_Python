from math import sqrt

def solution(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


num = int(input())

while 1:
    if not solution(num):
        print(num)
        break
    num += 1


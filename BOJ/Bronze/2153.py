from math import sqrt

def sol(n):
    if n == 1:
        return True
    else:
        for j in range(2, int(sqrt(n)) + 1):
            if n % j == 0:
                return False
        return True

s = input()
r = 0
for w in s:
    if w.islower():
        r += ord(w) - 96
    else:
        r += ord(w) - 38
if sol(r):
    print('It is a prime word.')
else:
    print('It is not a prime word.')

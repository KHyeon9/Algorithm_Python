from math import sqrt
k, l = map(int, input().split())
sieve = [True] * l
flag = True
for i in range(2, int(sqrt(l)) + 1):
    if sieve[i]:
        for j in range(i + i, l, i):
            sieve[j] = False
arr = [i for i in range(2, l) if sieve[i]]

for i in arr:
    if k % i == 0:
        flag = False
        break
if flag:
    print("GOOD")
else:
    print("BAD", i)
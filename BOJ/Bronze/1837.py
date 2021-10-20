from math import sqrt
p, k = map(int, input().split())
sieve = [True] * k
flag = True
for i in range(2, int(sqrt(k)) + 1):
    if sieve[i]:
        for j in range(i + i, k, i):
            sieve[j] = False
arr = [i for i in range(2, k) if sieve[i]]
for i in arr:
    if p % i == 0:
        flag = False
        break
if flag:
    print("GOOD")
else:
    print("BAD", i)
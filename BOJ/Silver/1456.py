from math import sqrt
a, b = map(int, input().split())
m = int(sqrt(b)) + 1
sieve = [False, False] + [True] * (m - 1)
for i in range(2, int(m ** 0.5) + 1):
    if sieve[i]:
        for j in range(i * 2, m, i):
            sieve[j] = False
prime_num = [i for i in range(m) if sieve[i]]
cnt = 0
for i in prime_num:
    n = 2
    while i ** n <= b:
        if a <= i ** n <= b:
            cnt += 1
        n += 1

print(cnt)

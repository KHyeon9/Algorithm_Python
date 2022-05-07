MAX = 10001
sieve = [False, False] + [True] * MAX

for i in range(2, int(MAX ** 0.5) + 1):
    if sieve[i]:
        for j in range(i * 2, MAX, i):
            sieve[j] = False
for _ in range(int(input())):
    n = int(input())
    gap = 10000
    for i in range(2, n):
        if sieve[n - i] and sieve[i] and 0 <= n - i - i < gap:
            n1, n2 = i, n - i
    print(n1, n2)

m = 1000001
sieve = [False, False] + [True] * (m - 1)
for i in range(2, int(m ** 0.5) + 1):
    if sieve[i]:
        for j in range(i * 2, m, i):
            sieve[j] = False

n = int(input())
result = 0
for i in range(n, m):
    if sieve[i] and str(i) == str(i)[::-1]:
        result = i
        break
print(result if result != 0 else 1003001)



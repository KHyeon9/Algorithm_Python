a, b = map(int, input().split())
if b > 10000000: b = 10000000
sieve = [False, False] + [True] * b
for i in range(2, int(b ** 0.5) + 1):
    if sieve[i]:
        for j in range(i * 2, b + 1, i):
            sieve[j] = False
Prime = [i for i in range(a, b + 1) if sieve[i]]
for num in Prime:
    num = str(num)
    if num == num[::-1]:
        print(num)
print(-1)
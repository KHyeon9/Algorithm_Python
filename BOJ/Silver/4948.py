from sys import stdin
cover = 246913
sieve = [False, False] + [True] * cover
for i in range(2, int(cover ** 0.5) + 1):
    if sieve[i]:
        for j in range(i + i, cover, i):
            sieve[j] = False

while 1:
    n = int(stdin.readline())
    cnt = 0
    if n == 0:
        break
    for i in range(n + 1, 2 * n + 1):
        if sieve[i]:
            cnt += 1
    print(cnt)
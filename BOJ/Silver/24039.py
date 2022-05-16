n = int(input())

sieve = [True] * 105
Prime = []

for i in range(2, 105):
    if sieve[i]:
        Prime.append(i)
        for j in range(i + i, 105, i):
            sieve[j] = False


for i in range(len(Prime) - 1):
    num = Prime[i] * Prime[i + 1]
    if num > n:
        print(num)
        break

n = int(input())
sieve = [False, False] + [True] * n
for i in range(2, int(n ** 0.5) + 1):
    if sieve[i]:
        for j in range(i + i, n + 1, i):
            sieve[j] = False

prime = [i for i in range(n + 1) if sieve[i]]
for num in prime:
    temp = str(num)
    use_num = []
    while 1:
        total = 0
        for i in temp:
            total += int(i) ** 2
        if total in use_num:
            break
        if total == 1:
            print(num)
            break
        use_num.append(total)
        temp = str(total)

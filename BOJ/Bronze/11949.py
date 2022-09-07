n, m = map(int, input().split())
n_ticket = [int(input()) for _ in range(n)]

for i in range(1, m + 1):
    for j in range(1, len(n_ticket)):
        if n_ticket[j - 1] % i > n_ticket[j] % i:
            n_ticket[j - 1], n_ticket[j] = n_ticket[j], n_ticket[j - 1]

for i in n_ticket:
    print(i)
n, q = map(int, input().split())
days = [0] * (n + 1)

for _ in range(q):
    c, p, x = map(int, input().split())

    if c == 1:
        days[p] += x
    else:
        print(sum(days[p:x + 1]))
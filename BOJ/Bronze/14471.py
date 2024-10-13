n, m = map(int, input().split())
total = m - 1
not_winning = []

for _ in range(m):
    a, b = map(int, input().split())

    if a >= n:
        total -= 1
    else:
        not_winning.append(a)


if total == 0:
    print(0)
else:
    res = 0
    for el in sorted(not_winning, reverse=True):
        res += n - el
        total -= 1

        if total == 0:
            break

    print(res)
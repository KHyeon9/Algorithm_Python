res = 0
for _ in range(int(input())):
    a, d, g = map(int, input().split())
    total = a * (d + g)
    if a == d + g:
        total *= 2
    res = max(res, total)
print(res)
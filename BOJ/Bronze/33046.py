a, b = map(int, input().split())
c, d = map(int, input().split())

total = a + b + c + d
res = 0

for _ in range(total - 1):
    if res == 4:
        res = 1
        continue
    res += 1

print(res)
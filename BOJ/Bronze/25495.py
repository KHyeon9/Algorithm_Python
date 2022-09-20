n = int(input())
li = list(map(int, input().split()))
res, before = 0, 0
be = 2
for i in range(n):
    if li[i] == before:
        be *= 2
    else:
        be = 2
    res += be
    before = li[i]
    if res >= 100:
        be = 2
        res, before = 0, 0
print(res)


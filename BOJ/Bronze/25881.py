t, o = map(int, input().split())
for _ in range(int(input())):
    e = int(input())
    res = 0
    if e > 1000:
        res += t * 1000 + (e - 1000) * o
    else:
        res += t * e
    print(e, res)

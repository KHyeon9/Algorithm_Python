n = int(input())
now, res = 1, 0

while n >= now ** 2:
    n -= now ** 2
    res += 1
    now += 1

print(res)
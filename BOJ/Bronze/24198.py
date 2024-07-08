n = int(input())
res, cnt = [0, 0], 0

while n:
    cnt += 1
    res[cnt % 2] += (n + 1) // 2
    n //= 2

print(*res)
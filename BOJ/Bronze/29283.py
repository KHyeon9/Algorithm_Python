n = int(input())
res, cnt, num = 0, 1, 0

while n != num:
    res += 30 * cnt
    num += 1
    if num != 0 and num % 5 == 0:
        cnt += 1
print(res)
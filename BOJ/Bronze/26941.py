n = int(input())
pyramid = 0
res = 0
cnt = 1
while 1:
    pyramid += cnt ** 2
    cnt += 2

    if pyramid > n:
        break
    res += 1
print(res)

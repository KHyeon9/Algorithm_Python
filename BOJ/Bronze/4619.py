while 1:
    b, n = map(int, input().split())
    cnt = 0
    if b == 0 and n == 0:
        break
    while cnt ** n < b:
        cnt += 1
    if cnt ** n - b < b - ((cnt - 1) ** n):
        print(cnt)

    else:
        print(cnt - 1)

for _ in range(int(input())):
    s = input()
    maxCnt = 0
    cnt = 0
    for i in s:
        if i == 'U':
            cnt += 1
        else:
            break
        maxCnt = max(maxCnt, cnt)
    print(maxCnt)

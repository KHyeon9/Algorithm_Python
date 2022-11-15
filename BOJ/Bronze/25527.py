while 1:
    t = int(input())
    if t == 0:
        break
    dataSet = list(map(int, input().split()))
    cnt = 0

    for i in range(1, t - 1):
        if dataSet[i - 1] < dataSet[i] and dataSet[i] > dataSet[i + 1]:
            cnt += 1
    print(cnt)
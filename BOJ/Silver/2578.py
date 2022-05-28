def check(arr):
    cnt = 0
    for i in range(5):
        c = 0
        for j in range(5):
            if arr[i][j] == 0:
                c += 1
        if c == 5:
            cnt += 1

    for i in range(5):
        c = 0
        for j in range(5):
            if arr[j][i] == 0:
                c += 1
        if c == 5:
            cnt += 1

    zero1, zero2 = 0, 0
    for i in range(5):
        if arr[i][i] == 0:
            zero1 += 1
        if arr[i][4-i] == 0:
            zero2 += 1
    if zero1 == 5:
        cnt += 1
    if zero2 == 5:
        cnt += 1

    return cnt


binggo = [list(map(int, input().split())) for _ in range(5)]
call = []

for _ in range(5):
    call += list(map(int, input().split()))

for n in range(25):
    for i in range(5):
        for j in range(5):
            if binggo[i][j] == call[n]:
                binggo[i][j] = 0
        if check(binggo) >= 3:
            print(n + 1)
            exit()




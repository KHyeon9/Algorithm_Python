k = int(input())
for _ in range(k):
    p, m = map(int, input().split())
    arr = [0 for _ in range(m + 1)]
    cnt = 0
    for i in range(p):
        n = int(input())
        if arr[n] != 0:
            cnt += 1
        else:
            arr[n] = 1
    print(cnt)
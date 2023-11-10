h, w = map(int, input().split())
arr = [input() for _ in range(h)]

cnt_zero, cnt_one = 0, 0

for i in range(h):
    for j in range(w):
        if arr[i][j] == '0':
            cnt_zero += 1
        else:
            cnt_one += 1

print(cnt_zero if cnt_zero < cnt_one else  cnt_one)


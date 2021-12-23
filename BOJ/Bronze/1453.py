arr = [0] * 101
n = int(input())
p = list(map(int, input().split()))
cnt = 0
for i in p:
    if arr[i] == 0:
        arr[i] = 1
    else:
        cnt += 1
print(cnt)

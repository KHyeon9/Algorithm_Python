n = int(input())
cnt = 0
result = []
for i in range(1, n):
    arr = [n, n - i]

    while 1:
        if arr[-2] < arr[-1]:
            break
        else:
            arr.append(arr[-2] - arr[-1])
    if cnt < len(arr):
        cnt = len(arr)
        result = arr
print(cnt)
print(*result)


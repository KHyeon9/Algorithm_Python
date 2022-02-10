from sys import stdin
read = stdin.readline
arr = [int(read()) for _ in range(int(read()))]
last = arr[-1]
cnt = 1
for i in range(len(arr) - 1, -1, -1):
    if last < arr[i]:
        cnt += 1
        last = arr[i]
print(cnt)
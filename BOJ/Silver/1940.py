n = int(input())
m = int(input())
num = sorted(list(map(int, input().split())))
cnt = 0
start, end = 0, n - 1
Sum = 0
while start < end:
    Sum = num[start] + num[end]
    if Sum == m:
        cnt += 1
        start += 1
        end -= 1
    elif Sum > m:
        end -= 1
    else:
        start += 1

print(cnt)
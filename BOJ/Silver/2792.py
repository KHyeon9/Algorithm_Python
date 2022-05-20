import sys
input = sys.stdin.readline

n, m = map(int, input().split())
j = [int(input()) for _ in range(m)]
left, right = 1, max(j)
while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for i in j:
        cnt += i // mid
        if i % mid != 0:
            cnt += 1

    if cnt > n:
        left = mid + 1

    else:
        right = mid - 1
print(left)
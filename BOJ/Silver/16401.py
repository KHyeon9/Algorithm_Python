import sys
input = sys.stdin.readline

m, n = map(int, input().split())
cookies = list(map(int, input().split()))
left, right = 0, max(cookies)
max_l = 0
while left <= right:
    cnt = 0
    mid = (left + right) // 2
    if mid == 0:
        break
    for i in cookies:
        cnt += (i // mid)

    if cnt >= m:
        max_l = mid
        left = mid + 1
    else:
        right = mid - 1
print(max_l)


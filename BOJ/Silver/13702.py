import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mak = [int(input()) for _ in range(n)]
left, right = 1, max(mak)
result = 0

while left <= right:
    mid = (left + right) // 2
    cnt = sum([i // mid for i in mak])

    if cnt >= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)
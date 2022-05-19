import sys
input = sys.stdin.readline

s, c = map(int, input().split())
pa = [int(input()) for _ in range(s)]

start, end = 1, max(pa)
pa_result = 0
while start <= end:
    mid = (start + end) // 2
    cnt = sum(i // mid for i in pa)
    if cnt >= c:
        pa_result = max(pa_result, mid)
        start = mid + 1
    else:
        end = mid - 1
print(sum(pa) - pa_result * c)

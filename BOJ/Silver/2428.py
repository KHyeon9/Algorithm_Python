n = int(input())
p = sorted(list(map(float, input().split())))
result = 0
for i in range(n):
    start, end = i, n - 1
    while start <= end:
        mid = (start + end) // 2
        if p[i] >= p[mid] * 0.9:
            start = mid + 1
        else:
            end = mid - 1
    result += start - i - 1
print(result)
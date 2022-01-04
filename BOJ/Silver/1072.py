def binary(x, y):
    start, end = 0, x
    first = y * 100 // x
    while start <= end:
        mid = (start + end) // 2
        second = (y + mid) * 100 // (x + mid)
        if first >= second:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    return answer


X, Y = map(int, input().split())
if Y * 100 // X >= 99:
    print(-1)
else:
    print(binary(X, Y))
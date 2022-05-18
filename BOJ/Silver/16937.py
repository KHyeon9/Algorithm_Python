h, w = map(int, input().split())
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = arr[i]
        x2, y2 = arr[j]

        if (x1 + x2 <= h and max(y1, y2) <= w) or (y1 + y2 <= h and max(x1, x2) <= w):
            result = max(result, x1 * y1 + x2 * y2)
        if (x1 + x2 <= w and max(y1, y2) <= h) or (y1 + y2 <= w and max(x1, x2) <= h):
            result = max(result, x1 * y1 + x2 * y2)
        if (x1 + y2 <= h and max(y1, x2) <= w) or (y1 + x2 <= h and max(x1, y2) <= w):
            result = max(result, x1 * y1 + x2 * y2)
        if (x1 + y2 <= w and max(y1, x2) <= h) or (y1 + x2 <= w and max(x1, y2) <= h):
            result = max(result, x1 * y1 + x2 * y2)

print(result)

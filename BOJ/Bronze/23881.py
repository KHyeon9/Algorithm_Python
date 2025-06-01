n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for last in range(n - 1, 0, -1):
    max_idx = 0
    for i in range(1, last + 1):
        if arr[i] > arr[max_idx]:
            max_idx = i

    if max_idx != last:
        arr[max_idx], arr[last] = arr[last], arr[max_idx]
        cnt += 1
        if cnt == k:
            print(*sorted([arr[max_idx], arr[last]]))
            break
else:
    print(-1)
from sys import stdin

def binary(l, arr, target):
    start = 0
    end = l - 1
    while start < end:
        mid = (start + end) // 2
        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            return mid
    return start


n, m = map(int, stdin.readline().split())
points = sorted(list(map(int, stdin.readline().split())))
for _ in range(m):
    low, high = map(int, stdin.readline().split())

    low_idx = binary(n, points, low)
    S = low_idx if points[low_idx] >= low else low_idx + 1

    high_idx = binary(n, points, high)
    E = high_idx if points[high_idx] <= high else high_idx - 1

    print(E - S + 1)


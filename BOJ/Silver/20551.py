from sys import stdin


def bin(start, end, arr, target):
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            if end == mid:
                break
            else:
                end = mid
        elif target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
    if arr[mid] == target:
        return mid
    else:
        return -1


n, m = map(int, stdin.readline().split())
array = sorted([int(stdin.readline()) for _ in range(n)])
for _ in range(m):
    d = int(stdin.readline())
    print(bin(0, n - 1, array, d))


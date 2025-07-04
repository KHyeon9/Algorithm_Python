def selection_sort(arr, arr2):
    arr_len = len(arr)
    if arr == arr2:
        return 1

    for i in range(arr_len - 1, 0, -1):
        max_idx = i
        for j in range(i):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
        if arr == arr2:
            return 1
    return 0

n = int(input())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
print(selection_sort(nums1, nums2))
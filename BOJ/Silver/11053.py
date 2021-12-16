n = int(input())
nums = list(map(int, input().split()))
arr = [0] * n
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j] and arr[i] < arr[j]:
            arr[i] = arr[j]
    arr[i] += 1
print(max(arr))
nums = list(map(int, input().split()))
arr = sorted(nums)
while 1:
    if nums == arr:
        break
    for i in range(4):
        if nums[i] > nums[i + 1]:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            print(*nums)

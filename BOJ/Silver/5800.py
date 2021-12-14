for i in range(int(input())):
    nums = list(map(int, input().split()))
    nums = sorted(nums[1:], reverse=True)
    gap = 0
    for j in range(1, len(nums)):
        if nums[j - 1] - nums[j] > gap:
            gap = nums[j - 1] - nums[j]
    print(f'Class {i + 1}')
    print(f'Max {max(nums)}, Min {min(nums)}, Largest gap {gap}')

n = int(input())
nums = [i for i in range(1, n + 1)]
while len(nums) > 1:
    temp = []
    for i in range(len(nums)):
        if i % 2:
            temp.append(nums[i])
    nums = temp

print(*nums)
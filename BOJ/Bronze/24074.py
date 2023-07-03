n = int(input())
nums = list(map(int, input().split()))
max_index = nums.index(max(nums))

print(sum(nums[:max_index]))
print(sum(nums[max_index + 1:]))

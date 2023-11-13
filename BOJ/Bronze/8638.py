arr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = int(input())
nums = list(map(int, input().split()))
max_score = max(nums)

res = []

for num in nums:
    if max_score == num:
        p = nums.index(num)
        res.append(arr[p])
        nums[p] = -1

print(*res, sep='')


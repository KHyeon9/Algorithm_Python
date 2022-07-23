res = -1
x, y = 0, 0
for i in range(9):
    nums = list(map(int, input().split()))
    max_nums = max(nums)
    if res < max_nums:
        x = i + 1
        y = nums.index(max_nums) + 1
        res = max_nums
print(res)
print(x, y)
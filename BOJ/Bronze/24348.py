nums = sorted(list(map(int, input().split())))
res = max(
    nums[0] * nums[1] + nums[2],
    nums[0] + nums[1] * nums[2]
)

print(res)

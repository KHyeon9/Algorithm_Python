n = int(input())
nums = list(map(int, input().split()))
MAX = 0
Sum = 0
for i in range(n - 1):
    if nums[i] >= nums[i + 1]:
        Sum = 0
    else:
        Sum += nums[i + 1] - nums[i]
    if MAX < Sum:
        MAX = Sum
print(MAX)
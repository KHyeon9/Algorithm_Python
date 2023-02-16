n = int(input())
nums = list(map(int, input().split()))
point = nums[0]
res = 0
for i in range(1, n):
    if nums[i-1] != nums[i] - 1:
        res += point
        point = nums[i]
print(res + point)

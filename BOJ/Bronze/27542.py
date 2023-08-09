n = int(input())
nums = list(map(int, input().split()))

while len(nums) > 1:
    temp = []
    for i in range(len(nums) - 1):
        temp.append(abs(nums[i] - nums[i + 1]))
    nums = temp
print(nums[0])
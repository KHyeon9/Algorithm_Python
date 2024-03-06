nums = input()

for i in range(len(nums)):
    if int(nums[i]) != i + 1:
        print(-1)
        exit()
print(nums[-1])
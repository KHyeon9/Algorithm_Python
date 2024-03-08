n = int(input())
nums = list(map(int, input().split()))

for i in range(n):
    temp = nums[:i] + nums[i + 1:]

    if sum(temp) == nums[i]:
        print(i + 1)
        break
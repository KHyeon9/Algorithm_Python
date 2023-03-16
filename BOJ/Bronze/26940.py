n = int(input())
nums = list(map(int, input().split()))
res = 0
for i in range(1, n):
    if nums[i] > nums[i - 1]:
        res +=1
print(res)
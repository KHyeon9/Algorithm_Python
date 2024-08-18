n = int(input())
nums = list(map(int, input().split()))
max_cnt, cnt = 0, 2

for i in range(n - 2):
    if nums[i] <= nums[i + 1] <= nums[i + 2]:
        cnt = 2
    elif nums[i] >= nums[i + 1] >= nums[i + 2]:
        cnt = 2
    else:
        cnt += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)

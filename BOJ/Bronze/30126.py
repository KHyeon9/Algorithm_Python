n = int(input())
nums = list(map(int, input().split()))
cnt, now, res = 1, nums[0], 0

for i in range(1, n):
    if now >= nums[i]:
        res = max(res, cnt)
        cnt = 1
    else:
        cnt += 1
    now = nums[i]
res = max(res, cnt)
print(res)
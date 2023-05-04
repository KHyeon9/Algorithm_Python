n, k = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
flag = True

for i in range(n - 1, 0, -1):
    max_idx = nums.index(max(nums[:i + 1]))

    if max_idx != i:
        nums[max_idx], nums[i] = nums[i], nums[max_idx]
        cnt += 1
    if cnt == k:
        print(*nums)
        break

else:
    print(-1)

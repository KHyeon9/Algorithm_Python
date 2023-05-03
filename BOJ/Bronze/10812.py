n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j, k = map(int, input().split())
    change = nums[:i-1] + nums[k-1:j] + nums[i-1:k - 1] + nums[j:]
    nums = change
print(*nums)

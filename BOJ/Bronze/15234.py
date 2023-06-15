n, k = map(int, input().split())
nums = list(map(int, input().split()))
res = 0

for i in range(n):
    for j in range(i + 1, n):
        if nums[i] + nums[j] == k:
            res += 1
print(res)

n = int(input())
nums = list(map(int, input().split()))
max_res = -n

for i in range(n):
    res = nums[i] - (n - i)
    max_res = max(res, max_res)
print(max_res)
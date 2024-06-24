n = int(input())
nums = sorted([int(input()) for _ in range(n)])
res = nums[0]

for i in range(1, n):
    res = (res + nums[i]) / 2

print("%.6f" %res)

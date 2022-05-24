import sys
input = sys.stdin.readline

n, q = map(int, input().split())
nums = sorted(list(map(int, input().split())))
nums_sum = [0]
for i in range(n):
    nums_sum.append(nums_sum[i] + nums[i])

for _ in range(q):
    l, r = map(int, input().split())
    print(nums_sum[r] - nums_sum[l - 1])

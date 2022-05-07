n = int(input())
nums = list(map(int, input().split()))
accum = [nums[0]]
result = 0
for i in range(1, n):
    accum.append(nums[i] + accum[i - 1])

for i in range(n):
    num = nums[i] * (accum[n - 1] - accum[i])
    result += num
print(result)


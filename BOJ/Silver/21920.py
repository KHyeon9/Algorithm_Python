from math import gcd
n = int(input())
nums = list(map(int, input().split()))
num = int(input())
result = []
for i in range(n):
    if gcd(num, nums[i]) == 1:
        result.append(nums[i])
print(sum(result)/len(result))

from math import sqrt

nums = list(map(int, input().split()))
a, b = sorted(nums[:2])
c = nums[2]

print(c ** 2 - b if a == 0 else int(sqrt(a + b)))

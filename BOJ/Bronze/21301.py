from math import sqrt

nums = list(map(float, input().split()))
# 평균값
avg = sum(nums) / 10
res = 0
# 수에 평균값을 빼고 제곱
for num in nums:
    res += (num - avg) ** 2
# n - 1로 나누고 루트
res = sqrt(res / 9)

print("COMFY" if res <= 1 else "NOT COMFY")


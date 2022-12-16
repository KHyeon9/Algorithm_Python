n = int(input())
nums = list(map(float, input().split()))
result = 0
for num in nums:
    result += num ** 3
print(result ** (1/3))
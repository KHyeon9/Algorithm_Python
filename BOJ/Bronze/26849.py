nums = []

for _ in range(int(input())):
    a, b = map(int, input().split())
    nums.append(a / b)

print(f"{min(nums):.10f} {max(nums):.10f} {sum(nums):.10f}")
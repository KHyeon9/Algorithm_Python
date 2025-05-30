n = int(input())
p, q, r, s = map(int, input().split())
a1 = int(input())
nums = [a1]

for i in range(0, n - 1):
    if i % 2 == 0:
        nums.append(p * nums[i // 2] + q)
    else:
        nums.append(r * nums[i // 2] + s)
print(sum(nums))
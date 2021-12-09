l = int(input())
nums = list(map(int, input().split()))
MAX, c = 1, 1
for i in range(l - 1):
    if nums[i] <= nums[i + 1]:
        c += 1
    else:
        c = 1
    if c > MAX:
        MAX = c
c = 1
for i in range(l - 1):
    if nums[i] >= nums[i + 1]:
        c += 1
    else:
        c = 1
    if c > MAX:
        MAX = c
print(MAX)


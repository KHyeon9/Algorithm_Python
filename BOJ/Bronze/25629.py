from math import ceil

t = int(input())
nums = list(map(int, input().split()))

even, odd = 0, 0

for n in nums:
    if n % 2 != 0:
        odd += 1
    else:
        even += 1

print(1 if odd == ceil(t / 2) and even == t // 2 else 0)
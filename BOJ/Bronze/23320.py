n = int(input())
nums = list(map(int, input().split()))
x, y = map(int, input().split())
res = 0

for num in nums:
    if num >= y:
        res += 1
print(round(n * (x / 100)), res)
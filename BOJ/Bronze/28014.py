n = int(input())
height = list(map(int, input().split()))
res = 1

for i in range(n - 1):
    if height[i] <= height[i + 1]:
        res += 1
print(res)

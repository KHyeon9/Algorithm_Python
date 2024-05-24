n = int(input())
nums = list(map(int, input().split()))
arr = []
res = [0] * n

for i in range(n):
    arr.append([nums[i], i])

arr.sort()

for i in range(1, n + 1):
    res[arr[i - 1][1]] = i

print(*res)
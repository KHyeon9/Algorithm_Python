n = int(input())
nums = list(map(int, input().split()))
arr = []
res = 0
for i in range(80001):
    if i % 3 == 0 or i % 7 == 0:
        res += i
    arr.append(res)
for num in nums:
    print(arr[num])

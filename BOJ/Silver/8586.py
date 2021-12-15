n = int(input())
arr = [0] * 300
for i in range(n):
    arr[i] = int(input())
dp = [arr[0], arr[0] + arr[1], max(arr[1] + arr[2], arr[0] + arr[2])]
for i in range(3, n):
    result = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])
    dp.append(result)
print(dp[n - 1])

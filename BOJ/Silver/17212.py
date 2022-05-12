n = int(input())
dp = [0, 1, 1, 2, 2, 1, 2, 1]
for i in range(8, n + 1):
    c = min(dp[i - 7], min(dp[i - 5], min(dp[i - 2], dp[i - 1]))) + 1
    dp.append(c)
print(dp[n])
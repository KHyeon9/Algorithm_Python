mod = int(1e9)

dp = [[0] * 10 for _ in range(101)]

for i in range(1, 10):
    dp[1][i] = 1

res = 0
n = int(input())

for i in range(2, n + 1):
    for j in range(10):
        if j > 0:
            dp[i][j] += dp[i - 1][j - 1] % mod
        if j < 9:
            dp[i][j] += dp[i - 1][j + 1] % mod

for j in range(10):
    res += dp[n][j] % mod

print(sum(dp[n]) % mod)




h, n = map(int, input().split())
size = abs(h - n) + 1
if size == 1:
    print(1)
else:
    dp = [[0 for _ in range(size)]for _ in range(size)]
    for i in range(size):
        dp[0][i] = 1
    for i in range(1, size):
        for j in range(size):
            if i <= j:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    print(dp[size - 1][size - 1])
n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]
res = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            else:
                dp[i][j] = 1
            res = max(res, dp[i][j])

print(res ** 2)

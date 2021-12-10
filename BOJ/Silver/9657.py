dp = [1, 0, 1, 1, 1]
n = int(input())
for i in range(5, n):
    if dp[i - 1] == 1 and dp[i - 3] == 1 and dp[i - 4]:
        dp.append(0)
    else:
        dp.append(1)
print('SK' if dp[n - 1] else 'CY')
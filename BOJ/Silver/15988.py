from sys import stdin
dp = [1, 2, 4]
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    for i in range(len(dp), n):
        dp.append((dp[-1] + dp[-2] + dp[-3]) % 1000000009)
    print(dp[n - 1])

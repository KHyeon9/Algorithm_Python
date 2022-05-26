import sys
input = sys.stdin.readline

n = int(input())

t, p = [], []
dp = [0] * (n + 1)

for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

max_dp = 0

for i in range(n):
    max_dp = max(dp[i], max_dp)
    if i + t[i] <= n:
        dp[i + t[i]] = max(p[i] + max_dp, dp[i + t[i]])

print(max(dp))
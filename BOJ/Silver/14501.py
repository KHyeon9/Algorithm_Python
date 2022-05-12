n = int(input())
days = []
dp = [0] * (n + 1)
for _ in range(n):
    t, p = map(int, input().split())
    days.append((t, p))
for i in range(n):
    for j in range(i + days[i][0], n + 1):
        if dp[j] < dp[i] + days[i][1]:
            dp[j] = dp[i] + days[i][1]
print(max(dp))




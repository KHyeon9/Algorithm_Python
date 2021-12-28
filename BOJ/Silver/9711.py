from sys import stdin
dp = [1, 1]
for _ in range(2, 10001):
    dp.append(dp[-1] + dp[-2])
for i in range(1, int(stdin.readline()) + 1):
    p, q = map(int, stdin.readline().split())
    print(f"Case #{i}: {dp[p - 1] % q}")
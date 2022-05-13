import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleep = list(map(int, input().split()))
code_take = list(map(int, input().split()))
sleep_check = [0] * (n + 3)
take_check = [0] * (n + 3)
for i in sleep:
    sleep_check[i] = 1
for take in code_take:
    if sleep_check[take]:
        continue
    for i in range(take, n + 3, take):
        if i not in sleep:
            take_check[i] = 1
dp = [take_check[0]]
for i in range(1, n + 3):
    dp.append(dp[i - 1] + take_check[i])
for _ in range(m):
    s, e = map(int, input().split())
    print(e - s + 1 - (dp[e] - dp[s - 1]))

for _ in range(int(input())):
    n = int(input())
    dp = [1, 1, 2, 3]
    for i in range(4, n + 1):
        num = dp[-1] + dp[-2] - dp[-3]
        if i % 3 == 0:
            num += 1
        dp.append(num)
    print(dp[n])

while True:
    dp = [0, 1]
    t = int(input())

    if t == -1:
        break

    for _ in range(1, t):
        dp.append(dp[-1] + dp[-2])

    print(f"Hour {t}: {dp[t]} cow(s) affected")
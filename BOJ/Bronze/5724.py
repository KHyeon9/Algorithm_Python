while 1:
    n = int(input())
    if n == 0:
        break
    dp = [0]
    for i in range(1, n + 1):
        dp.append(dp[-1] + i ** 2)
    print(dp[-1])

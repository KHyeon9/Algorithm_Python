dp = [1, 1]
n = int(input())
while True:
    if sum(dp) >= n:
        print(len(dp))
        break

    dp.append(dp[-2] + dp[-1])

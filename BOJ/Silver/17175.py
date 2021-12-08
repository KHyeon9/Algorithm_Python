dp = [1, 1]
n = int(input())
for i in range(2, n + 1):
    dp.append((dp[-1] + dp[-2] + 1) % 1000000007)
print(dp[-1])
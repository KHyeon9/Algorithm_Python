n = int(input())
coin_f = list(map(int, input().split()))
coin_b = list(map(int, input().split()))
result = 0
for i in range(n):
    result += abs(coin_f[i]) + abs(coin_b[i])
print(result)

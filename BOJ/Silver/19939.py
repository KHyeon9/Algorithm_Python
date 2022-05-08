n, k = map(int, input().split())
min_total = k * (k + 1) // 2
if min_total > n:
    print(-1)

elif (n - min_total) % k == 0:
    print(k - 1)

else:
    print(k)
n = int(input())
d = list(map(int, input().split()))
res = [0] * n
res[0] = 1

for i in range(n - 1):
    res[d[i] + 1] = i + 2

print(*res)


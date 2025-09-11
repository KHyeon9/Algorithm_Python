from math import ceil

n, k = map(int, input().split())
half = ceil(n / 2)
buy = list(map(int, input().split()))
res = [1 if buy[i] <= half else n for i in range(k)]
print(*res)
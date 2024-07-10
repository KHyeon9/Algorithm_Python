from math import ceil
n, t = map(int, input().split())
m = int(input())
x, y = map(int, input().split())

out_time = m / (60 * x)
in_time = (n - m) / (60 * y)
res = max(out_time + in_time - t, 0)
print(ceil(res))
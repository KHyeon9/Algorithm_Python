from math import ceil

a, b, c = map(int, input().split())
t = int(input())
res = a if t > 0 else 0
t = max(0, t - 30)
res += ceil(t / b) * c

print(res)
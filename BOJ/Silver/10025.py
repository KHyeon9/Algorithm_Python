import sys
input = sys.stdin.readline
MAX = 1000001
pails = [0] * MAX
n, k = map(int, input().split())
for _ in range(n):
    g, x = map(int, input().split())
    pails[x] = g
step = k * 2 + 1
total = sum(pails[:step])
max_ice = total
for i in range(step, MAX):
    total += pails[i] - pails[i - step]
    max_ice = max(max_ice, total)
print(max_ice)
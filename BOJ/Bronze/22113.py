n, m = map(int, input().split())
bus = list(map(int, input().split()))
total_cost = [list(map(int, input().split())) for _ in range(n)]
res = 0

for i in range(m - 1):
    res += total_cost[bus[i] - 1][bus[i + 1] - 1]

print(res)

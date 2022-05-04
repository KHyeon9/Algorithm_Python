from sys import stdin

n = int(stdin.readline())
distance = list(map(int, stdin.readline().split()))
cost = list(map(int, stdin.readline().split()))[:-1]
min_cost = 1e9
result = 0
for i in range(n - 1):
    min_cost = min(min_cost, cost[i])
    result += min_cost * distance[i]

print(result)
from sys import stdin
input = stdin.readline

n, m, k = map(int, input().split())
goal_x, goal_y = 1, m + 1
res, now = -1, 1e9

for i in range(k):
    x, y = map(int, input().split())
    total = abs(goal_x - x) + abs(goal_y - y)
    if now > total:
        res = i + 1
        now = total
print(res)

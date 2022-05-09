from sys import stdin
input = stdin.readline
n = int(input())
result = 0
x_points = []
y_points = []
for _ in range(n):
    x, y = map(int, input().split())
    x_points.append(x)
    y_points.append(y)

mid_x = sorted(x_points)[n//2]
mid_y = sorted(y_points)[n//2]

for i in range(n):
    result += abs(mid_x - x_points[i]) + abs(mid_y - y_points[i])
print(result)
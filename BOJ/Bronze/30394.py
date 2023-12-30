min_y, max_y = 2e9, -2e9

for _ in range(int(input())):
    x, y = map(int, input().split())

    min_y = min(min_y, y)
    max_y = max(max_y, y)

print(max_y - min_y)
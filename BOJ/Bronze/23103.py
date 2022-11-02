t = int(input())
distance = [list(map(int, input().split()))]
result = 0

for _ in range(t - 1):
    x, y = map(int, input().split())
    result += abs(distance[-1][0] - x) + abs(distance[-1][1] - y)
    distance.append([x, y])

print(result)
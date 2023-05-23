n = int(input())
points = sorted(list(map(int, input().split())))
print(sum(points[1:-1]))


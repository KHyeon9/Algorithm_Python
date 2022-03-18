point = [6, 3, 2, 1, 2]
team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))
point1, point2 = 0, 0
for i in range(5):
    point1 += team1[i] * point[i]
    point2 += team2[i] * point[i]
print(point1, point2)
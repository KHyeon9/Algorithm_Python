n = int(input())
team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))
total1, total2 = 0, 0
res = 0

for i in range(1, n + 1):
    total1 += team1[i - 1]
    total2 += team2[i - 1]

    if total1 == total2:
        res = i

print(res)
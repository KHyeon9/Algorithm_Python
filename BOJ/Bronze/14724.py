admin = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT",
         "MOTION", "SPG", "COMON", "ALMIGHTY"]

score = [0] * len(admin)

n = int(input())
for i in range(9):
    point = list(map(int, input().split()))
    score[i] = max(point)
print(admin[score.index(max(score))])
lv, hit = input().split()
lv = int(lv)
score = 0
if hit == "bad":
    score = 200
elif hit == "cool":
    score = 400
elif hit == "great":
    score = 600
elif hit == "perfect":
    score = 1000

print(lv * score)
money = [1, 5, 10, 20, 50, 100]
max_money = 0
bag = list(map(int, input().split()))
res = 0

for i in range(6):
    total = money[i] * bag[i]
    if total >= max_money:
        max_money = total
        res = money[i]

print(res)

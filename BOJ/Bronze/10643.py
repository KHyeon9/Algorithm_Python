pizza = [int(input()) for _ in range(8)]
res = 0

for i in range(8):
    if i + 4 > 8:
        mushroom = sum(pizza[i:]) + sum(pizza[:(i + 4) % 8])
    else:
        mushroom = sum(pizza[i:i + 4])
    res = max(res, mushroom)
print(res)
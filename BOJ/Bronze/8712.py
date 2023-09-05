n = int(input())
num = 1
res = []
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(num)
        num += 1
    if i % 2 == 1:
        temp = sorted(temp, reverse=True)

    res.append(temp)

for line in res:
    print(*line)
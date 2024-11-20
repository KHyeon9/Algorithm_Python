time = list(map(int, input().split(":")))
res = 0

for i in range(3):
    for j in range(3):
        for k in range(3):
            if i != j != k and i != k:
                if 0 < time[i] <= 12 and 0 <= time[j] < 60 and 0 <= time[k] < 60:
                    res += 1
print(res)
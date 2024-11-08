line = list(map(int, input().split()))
rods = sorted([[line[i], line[i + 3]] for i in range(3)],
              key=lambda x: x[0], reverse=True)

l, total, res = line[6], 0, 0

while l > total and rods[0][1] + rods[1][1] + rods[2][1] > 0:
    for i in range(3):
        if rods[i][1] > 0:
            total += rods[i][0]
            rods[i][1] -= 1
            res += 1
            break

print(res if total >= l else 0)
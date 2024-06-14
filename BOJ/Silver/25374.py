grade = [0, 4, 11, 23, 40, 60, 77, 89, 96, 100, 101]
res = [0] * 9
n = int(input())
points = sorted(list(map(int, input().split())), reverse=True)
set_point = sorted(list(set(points)), reverse=True)
total, temp, idx = 0, 0, 0

for p in set_point:
    temp += points.count(p)
    total += points.count(p)

    if grade[idx + 1] <= total:
        res[idx] += temp
        temp = 0
        while grade[idx + 1] <= total:
            idx += 1

for el in res:
    print(el)
n = int(input())
exercise = [input() for _ in range(n)]
week = []

for el in exercise:
    if "rest" in el:
        week.append("😎")
    elif "leg" in el:
        week.append("🦵")
    else:
        week.append("💪")

day, idx = 0, 0
res = []

while day < 31:
    res.append(week[idx % n])

    day += 1
    idx += 1

    idx = idx % n
    if day % 7 == 0:
        print(day // 7, end=" ")
        print(*res)
        res = []
print(day // 7, end=" ")
print(*res)

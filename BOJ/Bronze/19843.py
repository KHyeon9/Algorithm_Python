days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
time, n = map(int, input().split())

for _ in range(n):
    line = list(input().split())
    # 날짜가 같은 경우
    if line[0] == line[2]:
        time -= int(line[3]) - int(line[1])
    # 날짜가 다른 경우
    else:
        day_idx1 = days.index(line[0])
        day_idx2 = days.index(line[2])
        time -= 24 * (day_idx2 - day_idx1) + int(line[3]) - int(line[1])
# 2일보다 큰 경우
if time > 48:
    print(-1)
# 값이 0보다 작은 경우
elif time <= 0:
    print(0)
else:
    print(time)

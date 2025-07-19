n = int(input())
times = []
teacher_time = 0

# 시간 계산 및 선생님 출근 시간 분리
for _ in range(n + 1):
    a, b = input().split()
    h, m = map(int, a.split(":"))
    total_time = h * 60 + m
    if b == "teacher":
        teacher_time = total_time
    else:
        times.append(total_time)

# 시작 시간 계산
start_h, start_m = map(int, input().split(":"))
start_time = start_h * 60 + start_m
res = 0

# 시간 비교
for time in times:
    if time >= start_time and time >= teacher_time:
        res += 1

print(res)

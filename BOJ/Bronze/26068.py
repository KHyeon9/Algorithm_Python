cnt = 0

for _ in range(int(input())):
    day = list(input().split('-'))
    if int(day[1]) <= 90:
        cnt += 1
print(cnt)
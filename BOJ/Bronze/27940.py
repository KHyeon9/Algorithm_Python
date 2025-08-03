from sys import stdin
input = stdin.readline

n, m, k = map(int, input().split())
farm = 0
break_time = -1

for time in range(m):
    t, r = map(int, input().split())
    # 첫번째 값은 무조건 변화
    farm += r
    # 층이 무너지는 경우 시간 기록
    if farm > k and break_time == -1:
        break_time = time + 1
# 층이 무너지는 경우
if break_time > -1:
    # 첫번째 값은 무조건 변화하므로 1 고정
    print(break_time, 1)
else:
    print(-1)
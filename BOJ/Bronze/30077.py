n, m, l = map(int, input().split())
times = [int(input()) for _ in range(n)]
res = 0
# 가장 빠른 사람
min_d = min(times) * m

for time in times:
    # 1바퀴 차이난 상태에서 가장 빠른 사람과 비교
    if min_d > time * (m - 1):
        res += 1
print(res)




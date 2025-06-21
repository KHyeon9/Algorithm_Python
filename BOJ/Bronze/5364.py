from math import sqrt

n = int(input())
now_x, now_y = map(int, input().split())
rex_x, res_y = -1, -1
min_dist = 1e9

for _ in range(n - 1):
    x, y = map(int, input().split())
    # 거리 계산
    dist = round(sqrt((now_x - x) ** 2 + (now_y - y) ** 2), 2)
    # 현재 저장한 거리보다 작은 경우
    if min_dist > dist:
        rex_x, res_y = x, y
        min_dist = dist
# 출력
print(now_x, now_y)
print(rex_x, res_y)
print(min_dist)
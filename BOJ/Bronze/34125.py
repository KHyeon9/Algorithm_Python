n, m = map(int, input().split())
seats = [list(map(int, input().split())) for _ in range(n)]
center = (m + 1) // 2
min_dist = 1e9
res = [-1]
# 한 칸씩 이동하며 검사
for r in range(n):
    for c in range(m):
        # 빈 자리일 경우
        if seats[r][c] == 0:
            # 센터와 거리 계산
            dist = (r + 1) + abs(center - (c + 1))
            # 저장된 최소 거리보다 작을 경우
            if dist < min_dist:
                min_dist = dist
                res = [r + 1, c + 1]
print(*res)

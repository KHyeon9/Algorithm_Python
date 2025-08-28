r, c = map(int, input().split())
a, b = map(int, input().split())
# 체스판의 행
for i in range(r):
    # 각 행을 A번 복제
    for _ in range(a):
        line = ""
        # 체스판의 열
        for j in range(c):
            # 각 칸을 너비 B만큼 확장
            line += ('X' if (i + j) % 2 == 0 else '.') * b
        print(line)

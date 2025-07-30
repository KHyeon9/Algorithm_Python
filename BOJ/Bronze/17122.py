board = [[0 for _ in range(8)] for _ in range(8)]
# 체스 보드 흑백 셋팅
for i in range(8):
    for j in range(8):
        board[i][j] = (i + j + 1) % 2

for _ in range(int(input())):
    a, b = input().split()
    # a의 x, y 죄표
    a_x = ord(a[0]) - ord('A')
    a_y = int(a[1]) - 1
    # b의 x, y 죄표
    b = int(b) - 1
    b_x = b % 8
    b_y = b // 8

    print("YES" if board[a_y][a_x] == board[b_y][b_x] else "NO")

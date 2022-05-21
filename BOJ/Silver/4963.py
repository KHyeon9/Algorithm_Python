import sys
sys.setrecursionlimit(10**6)

def solution(li, x, y):
    dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

    for i in range(9):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < h and 0 <= my < w:
            if li[mx][my] == 1:
                li[mx][my] = 0
                solution(li, mx, my)


while 1:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                cnt += 1
                solution(arr, i, j)

    print(cnt)
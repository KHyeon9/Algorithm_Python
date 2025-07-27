from sys import stdin
input = stdin.readline

n = int(input())
# 배열 생성
arr = [[-1] * 1001 for _ in range(1001)]

for t in range(n):
    a, b, w, h = map(int, input().split())
    # 색종이 범위에 따라 각각 arr에 기입
    for y in range(b, b + h):
        arr[y][a:a + w] = [t] * w
# 각 색종이 갯수 출력
for t in range(n):
    res = 0
    for line in arr:
        res += line.count(t)
    print(res)

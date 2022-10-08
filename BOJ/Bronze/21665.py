n, m = map(int, input().split())
bef = [list(input()) for _ in range(n)]
space = input()
aft = [list(input()) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        if bef[i][j] == 'B':
            bef[i][j] = 'W'
        else:
            bef[i][j] = 'B'
for i in range(n):
    for j in range(m):
        if bef[i][j] != aft[i][j]:
            cnt += 1
print(cnt)
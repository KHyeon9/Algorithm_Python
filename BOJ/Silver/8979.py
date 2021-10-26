n, k = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(n)]
m.sort(key=lambda x: (-x[1], -x[2], -x[3]))
for i in range(n):
    if m[i][0] == k:
        num = i
        break
for i in range(n):
    if m[num][1:] == m[i][1:]:
        print(i + 1)
        break
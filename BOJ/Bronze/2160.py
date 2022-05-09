n = int(input())
arr = []
max_cnt = -1
r1, r2 = 0, 0

for _ in range(n):
    a = []
    for _ in range(5):
        a.append(input())
    arr.append(a)

for i in range(n):
    for j in range(i + 1, n):
        cnt = 0
        for x in range(5):
            for y in range(7):
                if arr[i][x][y] == arr[j][x][y]:
                    cnt += 1
        if max_cnt < cnt:
            max_cnt = cnt
            r1 = i
            r2 = j
print(r1 + 1, r2 + 1)

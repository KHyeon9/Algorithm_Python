n = int(input())
arr = [input() + 'X' for _ in range(n)]
arr.append('x' * (n + 1))
r1, r2 = 0, 0

for i in range(n + 1):
    cnt1, cnt2 = 0, 0
    for j in range(n + 1):
        if arr[i][j] == '.':
            cnt1 += 1
        else:
            if cnt1 >= 2:
                r1 += 1
            cnt1 = 0

        if arr[j][i] == '.':
            cnt2 += 1
        else:
            if cnt2 >= 2:
                r2 += 1
            cnt2 = 0
print(r1, r2)

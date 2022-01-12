n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
answer = 0
for i in range(n):
    l = 0
    for j in range(m):
        if arr[i][j] == '-':
            l += 1
            continue
        else:
            if l > 0:
                answer += 1
            l = 0
    if l > 0:
        answer += 1
for i in range(m):
    l = 0
    for j in range(n):
        if arr[j][i] == '|':
            l += 1
            continue
        else:
            if l > 0:
                answer += 1
            l = 0
    if l > 0:
        answer += 1
print(answer)
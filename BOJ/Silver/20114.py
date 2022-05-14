n, h, w = map(int, input().split())
li = [input() for _ in range(h)]
result = ['?'] * n

for i in range(h):
    p = 0
    for j in range(0, n * w, w):
        line = li[i][j:j + w].strip('?')
        if result[p] == '?' and line:
            result[p] = line[0]
        p += 1

print(*result, sep='')


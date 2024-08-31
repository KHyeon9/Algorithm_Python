n = int(input())
arr = [input() for _ in range(n)]
res = 1

for x in range(n):
    line = arr[x]

    if line.count('B') > n // 2 or line.count('W') > n // 2:
        res = 0

    if 'BBB' in line or 'WWW' in line:
        res = 0

if res == 1:
    for x in range(n):
        line = ""
        for y in range(n):
            line += arr[y][x]

        if line.count('B') > n // 2 or line.count('W') > n // 2:
            res = 0

        if 'BBB' in line or 'WWW' in line:
            res = 0
print(res)
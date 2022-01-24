from sys import stdin
n = int(stdin.readline())
m = int(stdin.readline())
s = stdin.readline()
cnt, i, result = 0, 0, 0
while i < (m - 1):
    if s[i:i + 3] == 'IOI':
        i += 2
        cnt += 1
        if cnt == n:
            result += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0
print(result)
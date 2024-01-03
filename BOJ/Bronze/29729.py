from sys import stdin

s, n, m = map(int, stdin.readline().split())

cnt = 0

for _ in range(n + m):
    num = int(stdin.readline())

    if num == 1:
        if s == cnt:
            s += s
        cnt += 1
    else:
        cnt -= 1

print(s)
n, h = map(int, input().split())
cnt = 0

for a in list(map(int, input().split())):
    if a <= h:
        cnt += 1

print(cnt)
n, m = map(int, input().split())
cnt = 0
for _ in range(n):
    score = list(map(int, input().split()))
    if score.count(0) == 0:
        cnt += 1
print(cnt)

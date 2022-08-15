import sys
input = sys.stdin.readline

n, k, l = map(int, input().split())
result = []
for _ in range(n):
    ratings = list(map(int, input().split()))
    cnt = 0
    if sum(ratings) >= k:
        for i in ratings:
            if i < l:
                break
            cnt += 1
    if cnt == 3:
        result += ratings
print(len(result) // 3)
print(*result)
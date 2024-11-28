n = int(input())
picture = [list(map(int, input().split())) for _ in range(n)]
res = 0

for i in range(1, n):
    res = max(
        res,
        (picture[i][1] - picture[i - 1][1]) // (picture[i][0] - picture[i - 1][0])
    )

print(res)
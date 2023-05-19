n, m = map(int, input().split())
cnt = 0
lalpa = list(map(int, input().split()))

for _ in range(n - 1):
    streamer = list(map(int, input().split()))
    gap = 0
    for i in range(m):
        gap += abs(lalpa[i] - streamer[i])

    if gap > 2000:
        cnt += 1

if (n - 1) / 2 <= cnt:
    print("YES")
else:
    print("NO")
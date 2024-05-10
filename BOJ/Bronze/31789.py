n = int(input())
x, s = map(int, input().split())
res = 0

for _ in range(n):
    c, p = map(int, input().split())

    if x >= c:
        res = max(res, p)

print("YES" if res > s else "NO")

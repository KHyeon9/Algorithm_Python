n, s = map(int, input().split())
res = 0
for _ in range(n):
    speed = int(input())
    if res > s:
        res -= 1
    res += speed

print(res)




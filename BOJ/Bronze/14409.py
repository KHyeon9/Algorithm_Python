n = int(input())
x = int(input())
res = 0

for _ in range(n):
    p1, p2 = map(int, input().split())

    if abs(p1 - p2) <= x:
        res += max(p1, p2)
    else:
        res += int(input())
print(res)
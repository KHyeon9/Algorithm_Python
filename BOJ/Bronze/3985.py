cake = [0] * (int(input()) + 1)
n = int(input())
arr = [0] * (n + 1)
max_p, max_p2 = 0, 0
r1, r2 = 0, 0
for num in range(1, n + 1):
    p, k = map(int, input().split())
    cnt = k - p + 1
    cnt2 = 0
    for i in range(p, k + 1):
        if cake[i] == 0:
            cake[i] = 1
            cnt2 += 1
    if cnt > max_p:
        max_p = cnt
        r1 = num
    if cnt2 > max_p2:
        max_p2 = cnt2
        r2 = num
print(r1)
print(r2)

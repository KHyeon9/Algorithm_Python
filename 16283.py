a, b, n, w = map(int, input().split())
flag = 0
for i in range(1, n):
    if a * i + b * (n - i) == w:
        flag += 1
        r1 = i
        r2 = n - i
if flag == 1:
    print(r1, r2)
else:
    print(-1)
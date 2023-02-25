n = int(input())
res = 0

for i in range(n):
    h, b, k = map(int, input().split())
    buy = b - h
    if buy > 0:
        res += buy * k

print(res)
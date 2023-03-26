xZero, n = map(int, input().split())

for i in range(n):
    if xZero % 2 == 0:
        xZero = (xZero // 2) ^ 6
    else:
        xZero = (xZero * 2) ^ 6

print(xZero)

n = int(input())
tips = sorted([int(input()) for _ in range(n)], reverse=True)
total_tip = 0
for i in range(n):
    tip = tips[i] - i
    if tip < 0:
        tip = 0
    total_tip += tip
print(total_tip)
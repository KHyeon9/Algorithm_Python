n, k = map(int, input().split())
total, max_stand = 0, 0

for _ in range(n):
    a, b = map(int, input().split())
    total += a - b

    if total > k:
        max_stand = max(max_stand, total - k)

print(max_stand)
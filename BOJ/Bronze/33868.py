max_t, min_l = 0, 1e9

for _ in range(int(input())):
    t, b = map(int, input().split())
    max_t = max(max_t, t)
    min_l = min(min_l, b)

print(max_t * min_l % 7 + 1)
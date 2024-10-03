n, k = map(int, input().split())
safe_h, broken_h = 1, k

for i in range(n):
    h, res = input().split()
    h = int(h)

    if res == "SAFE":
        safe_h = max(h, safe_h)
    else:
        broken_h = min(h, broken_h)

print(safe_h + 1, broken_h - 1)


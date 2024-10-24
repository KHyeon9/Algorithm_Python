n, c = map(int, input().split())
h, w = n, n

for _ in range(c):
    x, y = map(int, input().split())

    if x >= w or y >= h:
        continue

    if h * x >= w * y: w = x
    else: h = y

print(h * w)
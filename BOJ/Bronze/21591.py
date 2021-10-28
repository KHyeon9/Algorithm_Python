w, c, w2, c2 = map(int, input().split())
r1 = w - w2
r2 = c - c2
if r1 <= 1 or r2 <= 1:
    print(0)
else:
    print(1)
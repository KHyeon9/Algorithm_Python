w, h, d = map(int, input().split())

w -= d * 2
h -= d * 2

if w <= 0 or h <= 0:
    print(0)
else:
    print(w * h)
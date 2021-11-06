from math import floor
while 1:
    a, b, c, d = map(int, input().split())
    if a == b == c == d == 0:
        break
    r = min(max(c, d) / max(a, b), min(c, d) / min(a, b))
    if r >= 1:
        print("100%")
    else:
        print(f"{floor(r * 100)}%")
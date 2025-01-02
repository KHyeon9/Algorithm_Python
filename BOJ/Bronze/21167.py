from math import sqrt

while True:
    try:
        r, s = input().split()
        r, s = int(r), float("0" + s)
        res = sqrt(r * (s + 0.16) / 0.067)
        print(round(res))
    except EOFError:
        break
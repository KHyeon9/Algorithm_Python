from math import sqrt

n, w, h = list(map(int, input().split()))

b = sqrt(w * w + h * h)

for i in range(n):
    l = int(input())

    if l <= b:
        print("DA")

    else:
        print("NE")
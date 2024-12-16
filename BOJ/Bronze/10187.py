from math import sqrt
golden_ratio = (1 + sqrt(5)) / 2

for _ in range(int(input())):
    a, b = map(float, input().split())

    if a < b:
        a, b = b, a

    if golden_ratio * 0.99 <= a / b <= golden_ratio * 1.01:
        print("golden")
    else:
        print("not")
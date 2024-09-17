a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

total1, total2 = a1 + b1 * 2 + c1 * 3, a2 + b2 * 2 + c2 * 3

if total1 > total2:
    print(1)
elif total1 < total2:
    print(2)
else:
    print(0)
a1, a2, b1, b2 = 0, 0, 0, 0

for _ in range(int(input())):
    e, v1, v2 = map(int, input().split())

    a1 += v1
    b1 += v2

    if v1 > v2:
        a2 += e
    elif v1 < v2:
        b2 += e

if a1 > b1 and a2 > b2:
    print(1)
elif a1 < b1 and a2 < b2:
    print(2)
else:
    print(0)
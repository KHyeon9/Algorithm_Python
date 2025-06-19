for _ in range(int(input())):
    a, b, c = map(int, input().split())
    total = a * 0.15 + b * 0.2 + c * 0.25
    res = 0
    flag = True

    while total + res * 0.4 < 90:
        res += 1
        if res > 100:
            flag = False
            break
    print(res if flag else "impossible")

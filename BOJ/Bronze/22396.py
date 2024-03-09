while True:
    ru, wa, c, r = map(int, input().split())

    if ru == wa == c == r == 0:
        break

    i = 0
    while True:
        if ru + r * i >= c * wa:
            print(i)
            break
        i += 1
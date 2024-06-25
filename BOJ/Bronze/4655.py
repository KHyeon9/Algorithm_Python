while True:
    n = float(input())

    if n == 0:
        break

    l, res = 2, 0

    while res < n:
        res += 1 / l
        l += 1

    print(f"{l - 2} card(s)")

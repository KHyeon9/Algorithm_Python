res = 0

while True:
    try:
        s, x = input().split()
        x = int(x)
        if s == "Es":
            res += 21 * x
        else:
            res += 17 * x

    except EOFError:
        break

print(res)


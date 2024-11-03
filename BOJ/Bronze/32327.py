res = int(input())

while True:
    try:
        d = int(input())

        if d >= res:
            break

        res += d

    except EOFError:
        break

print(res)